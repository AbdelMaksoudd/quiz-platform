# 📘 Quiz Platform

### 🎥 Video Demo  
[▶️ Watch Demo](https://youtu.be/c2fNxOZYqSU)

---

## 📝 Description
The **Quiz Platform** is a web-based application built as the final project for **Harvard CS50x**.  

It provides an easy way for teachers to:
- Create quizzes with multiple-choice questions  
- Generate unique codes for exams  
- View student results in real-time  

And for students to:
- Join quizzes using a shared code  
- Answer questions online  
- Get instant grading and feedback  

---

## 🚀 Features
- 🔑 **Authentication**: Register & log in (students/teachers)  
- 📝 **Create Quizzes**: Add questions & options dynamically  
- 🎯 **Real-time Grading**: Instant evaluation of answers  
- 📊 **Dashboard**: Teachers can track student performance  
- 👤 **About Page**: Includes developer info + LinkedIn integration  

---

## 🛠️ Technologies Used
- **Backend**: Python (Flask), SQLite (via CS50 Library)  
- **Frontend**: HTML, CSS, JavaScript  
- **Templating**: Jinja2  
- **Other**: Flask-Login, CS50 Library  

---

## 📂 Project Structure
## Project Structure

```plaintext
quiz-platform/  
│  
├── static/                 # CSS and static assets (images, scripts)  
│  
├── templates/              # HTML templates  
│   ├── about.html          # About page with developer info + LinkedIn badge  
│   ├── answer.html         # Page showing the student's score/result after submission  
│   ├── code.html           # Form page where student enters exam code to start quiz  
│   ├── create.html         # Teacher quiz creation page (dynamic add questions)  
│   ├── dashboard.html      # Teacher dashboard: table of students/scores/exams  
│   ├── done.html           # Confirmation page showing generated exam code after create  
│   ├── home.html           # Home / landing page  
│   ├── layout.html         # Base template (navigation, flash/message area)  
│   ├── login.html          # Login form  
│   ├── quiz.html           # Quiz-taking page (renders questions and radio inputs)  
│   ├── register.html       # Registration form for new users  
│   └── test.html           # Optional: debug/test template used during development  
│  
├── app.py                  # Main Flask application (routes, DB usage)  
├── helpers.py              # Helper functions (login_required, generate_exam_code, etc.)  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation
```  
---

## ⚡ Installation & Usage
1. Clone the repository:
   
   git clone https://github.com/AbdelMaksoudd/quiz-platform.git
   
   cd quiz-platform

3. Install dependencies:
   
   pip install -r requirements.txt

5. Run the Flask server:
   
   flask run

7. Open in your browser:
   
   http://127.0.0.1:5000/

---

## 🔮 Future Improvements
- Randomize question order  
- Add essay-type questions  
- Mobile optimization  
- Advanced teacher analytics  

---

## 🙌 Acknowledgments
This project was created as part of **CS50x: Introduction to Computer Science** by Harvard University.  
Special thanks to the CS50 staff and community for their guidance.  

---

✨ *Made with passion for learning and teaching.*

