from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, generate_exam_code
import string
from flask import url_for



app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///exams.db")


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/login", methods=["GET", "POST"])
def login():



    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        # Ensure username was submitted
        if not request.form.get("username"):
            return {"status": "error", "message": "must provide username"}

        # Ensure password was submitted
        elif not request.form.get("password"):
            return {"status": "error", "message": "Must provide password"}



        # Ensure username exists and password is correct
        elif len(rows) != 1 or not check_password_hash(
            rows[0]["password_hash"], request.form.get("password")
        ):
            return {"status": "error", "message": "invalid username and/or password"}

        else:
            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]
            # Redirect user to home page
        return {"status": "success", "message": "Login successfully!", "redirect": "/"}

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        session.pop("exam_id", None)
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():

    """Log user out"""

    session.clear()
    session.pop("exam_id", None)

    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        repassword = request.form.get("confirmation")
        if not name:
            return {"status": "error", "message": "Must provide username"}

        elif not password:
            return {"status": "error", "message": "Must provide password"}

        elif not repassword:
            return {"status": "error", "message": "Must confirm password"}


        elif password != repassword:
            return {"status": "error", "message": "must confirm password matches password"}
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)
        if len(rows) > 0:
            return {"status": "error", "message": "username already taken"}

        hash_pass = generate_password_hash(password)
        new_user_id = db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", name, hash_pass)
        session["user_id"] = new_user_id

        return {"status": "success", "message": "Registered successfully!", "redirect": "/"}

    else:
        session.pop("exam_id", None)
        return render_template("register.html")

@app.route("/code", methods=["GET", "POST"])
@login_required
def code():
    if request.method == "POST":
        code = request.form.get("code")

        if not code:
            return {"status": "error", "message": "Must provide code"}

        rows = db.execute("SELECT id FROM exams WHERE code = ?", code)
        if len(rows) == 0:
            return {"status": "error", "message": "Invalid code"}

        else:
            session["exam_id"] = rows[0]["id"]
            questions = db.execute("SELECT * FROM questions WHERE exam_id = ?", session["exam_id"])
            exam = db.execute("SELECT * FROM exams WHERE id = ?", session["exam_id"])[0]


        #return {"status": "success", "message": "Code accepted", "redirect": url_for("quiz")}
        return render_template("quiz.html", questions=questions, exam = exam)

    else:
        session.pop("exam_id", None)
        return render_template("code.html")




@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    score = 0
    count = 0
    if request.method == "POST":
        exam_id= session["exam_id"]
        questions = db.execute("SELECT * FROM questions WHERE exam_id = ?", exam_id)
        for q in questions:
                answer = request.form.get(f"answer_{q['id']}")
                if answer.upper() == q['correct_ans'].upper():
                    score +=1
        for i in range(len(questions)):
            count+=1
        db.execute(
            "INSERT INTO results (exam_id, student_id, score) VALUES (?, ?, ?)",
            exam_id, session["user_id"], score
        )
        session.pop("exam_id", None)
        return render_template("answer.html", score=score, count = count)

    else:
        session.pop("exam_id", None)
        return render_template("code.html")




@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title")
        if not title:
            return {"status": "error", "message": "Exam title is required"}
        code = generate_exam_code()
        teacher_id = session["user_id"]
        description = request.form.get("description")
        questions = request.form.getlist("question[]")
        if not any(q.strip() for q in questions):
            return {"status": "error", "message": "At least one question is required"}
        options_a = request.form.getlist("option_a[]")
        options_b = request.form.getlist("option_b[]")
        options_c = request.form.getlist("option_c[]")
        options_d = request.form.getlist("option_d[]")
        exam_id = db.execute(
            "INSERT INTO exams (title, description, code, teacher_id) VALUES (?, ?, ?, ?)",
            title, description, code, teacher_id
        )

        for i in range(len(questions)):
            if questions[i].strip():
                correct = request.form.get(f"correct_{i}")
                if not correct:
                    return {"status": "error", "message": "must mark the correct answer"}
                db.execute(
                    "INSERT INTO questions (exam_id, question, option_a, option_b, option_c, option_d, correct_ans) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    exam_id, questions[i], options_a[i], options_b[i], options_c[i], options_d[i], correct
                )
        return render_template("done.html", code=code)

    else:
        return render_template("create.html")



@app.route("/dashboard")
@login_required
def dashboard():
    rows = db.execute("SELECT exams.title AS exam_title, users.username AS student_name, results.score, COUNT(questions.id) AS num FROM results JOIN users ON results.student_id = users.id JOIN exams ON results.exam_id = exams.id JOIN questions ON questions.exam_id = exams.id WHERE exams.teacher_id = ? GROUP BY results.id", session["user_id"])
    return render_template("dashboard.html", rows=rows)




@app.route("/About_Me")
def about():
    return render_template("about.html")

