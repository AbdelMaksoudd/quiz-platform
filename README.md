# 📘 Quiz Platform

### 🎥 Video Demo  
[▶️ Watch Demo](https://youtu.be/YOUR_VIDEO_LINK)

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
quiz-platform/
│
├── static/             # CSS and static assets
├── templates/          # HTML templates
│   ├── layout.html     # Base template
│   ├── create.html     # Quiz creation
│   ├── quiz.html       # Quiz page for students
│   ├── dashboard.html  # Teacher's dashboard
│   └── about.html      # About page
│
├── app.py              # Main Flask app
├── helpers.py          # Helper functions
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

---

## ⚡ Installation & Usage
1. Clone the repository:
   git clone https://github.com/AbdelMaksoudd/quiz-platform.git
   cd quiz-platform

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask server:
   flask run

4. Open in your browser:
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

