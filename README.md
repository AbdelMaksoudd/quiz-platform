# Quiz Platform
#### Video Demo: <URL HERE>
#### Description:

## Overview
This project is a **web-based quiz platform** built as part of the CS50 final projet. The main purpose of this application is to allow teachers to create quizzes, manage questions, and view results, while students can log in, take those quizzes, and immediately receive scores. It is designed using **Flask** as the backend framework, **SQLite from cs50 library** as the database, and **HTML, CSS, and JavaScript** for the frontend.

The project simulates a real-world use case where institutions, schools, or individual teachers might need an easy and effective way to evaluate students. Unlike static paper-based quizzes, this system provides automation, real-time grading, and an intuitive user interface.

---

## Features
1. **User Authentication**
   - Students and teachers can register and log in.
   - Flask-Login is used to restrict access to certain pages.

2. **Quiz Creation**
   - Teachers can create a quiz by entering a title, description, and multiple questions.
   - Each question can have four options (A, B, C, D), with one correct answer.
   - When you create an exam, a random code of numbers and letters is automatically generated.

3. **Quiz Taking**
   - Students can attempt quizzes assigned by teachers by enter the code created with the teacher after logging in.
   - The system evaluates the answers automatically and calculates the score.

4. **Dashboard**
   - Teachers have access to a dashboard to view student names, exam titles, scores, and number of questions.
   - A scrollable table allows teachers to easily navigate through many results.

5. **About Page**
   - A personalized page introduces the developer, including name, GitHub, LinkedIn, city, and project title.

---

## File Structure and Functionality
1. **app.py (Flask app)**
   - Contains all the routes for login, logout, quiz creation, quiz attempt, result submission, and dashboard.
   - Handles database queries and integrates the templates.

2. **templates/layout.html**
   - The base template that defines the structure and navigation bar of the site.
   - Other pages extend this file to maintain consistency.

3. **templates/create.html**
   - Form where teachers input quiz data.
   - Includes JavaScript that dynamically adds new question fields without refreshing the page.

4. **templates/quiz.html**
   - Displays a quiz to the student with multiple-choice questions.
   - Radio buttons are used to select answers.
   - Form submission posts data back to the Flask app for grading.

5. **templates/answer.html**
   - Shows the student’s score out of the total number of questions.

6. **templates/dashboard.html**
   - Displays a table containing exam titles, student usernames, their scores, and question counts wich created by a currently logged-in user or teacher.
   - CSS ensures that the table is styled cleanly and scrollable for large datasets.

7. **templates/about.html**
   - A personal “About Me” page with information about the developer and an embedded LinkedIn badge.

8. **templates/code.html**
   - Form to receive the code to take you to the exam page.

9. **templates/done.html**
   - Show the code that was created for a specific exam

10. **templates/home.html**
   - home page just nothing.

11. **templates/login.html**
   - Log in if the user exists and the password is correct.

12. **templates/register.html**
   - Create an account and automatically log in.

13. **static/styles.css**
   - Central stylesheet defining the design of forms, buttons, tables, and containers.

14. **Database (SQLite)**
   - `users` table: stores student and teacher accounts.
   - `exams` table: stores quizzes created by teachers.
   - `questions` table: stores all questions linked to an exam.
   - `results` table: stores student submissions with scores.

---

## Design Choices
While developing the project, several design decisions were made:

- **Correct Answer Storage:**
  Instead of storing the entire text of the correct option, the system stores only a single letter (`a`, `b`, `c`, or `d`). This makes the database smaller and faster to query. However, it required careful matching between submitted answers and stored values.

- **Dynamic Question Creation:**
  A JavaScript function was implemented to let teachers add questions dynamically. This design choice improves usability and avoids the need to reload or manually add multiple forms.

- **Session Management:**
  Flask sessions were used to temporarily store data such as the current exam being attempted. This makes the application lightweight while maintaining state.

- **Dashboard Scroll:**
  Since results could be large in number, CSS was used to provide a scrollable table rather than overwhelming the user with an extremely long page.

- **Separation of Concerns:**
  The project followed Flask’s philosophy of separating templates, static files, and application logic. This makes it easier to maintain and expand in the future.

---

## Challenges Faced
1. **Answer Matching:**
   Initially, student answers were not matching the correct answers because of case sensitivity. The solution was to normalize both values to lowercase before comparison.

2. **Session Errors:**
   Accidentally popping session variables too early caused loss of exam IDs during submission. This was fixed by restructuring the route logic.

3. **Database Queries:**
   Writing efficient SQL JOIN statements to fetch student results with usernames, exam titles, and scores was challenging but essential for the dashboard.

---

## Future Improvements
- **Question Randomization:**
  Shuffle the order of questions and answers to make quizzes less predictable.

- **Exam Deadlines:**
  Allow teachers to set start and end times for each quiz.

- **Advanced Analytics:**
  Provide teachers with statistics such as average scores, most frequently wrong answers, and performance over time.

- **Mobile Optimization:**
  Enhance CSS further for smaller screens to ensure usability on phones.

- **Essay Questions:**
  Add essay questions and send them to the teacher.

---

## Conclusion
This quiz platform demonstrates a practical use of **Flask, SQL, and web development** concepts. It covers authentication, form handling, database operations, frontend design, and integration of third-party tools like LinkedIn badges. While simple in appearance, it incorporates multiple programming paradigms: procedural, object-oriented (Flask classes), and declarative (SQL). The project reflects the culmination of CS50’s teachings by turning theory into a complete, working product.

Overall, this README explains the architecture, purpose, design decisions, and potential extensions of the quiz platform. The final application is a functional, user-friendly tool that could be used in educational environments to streamline assessments.

---
