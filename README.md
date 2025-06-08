# 📕 Student Grading System (Tkinter app)

A desktop application using Python Tkinter that enables administrators, teachers, and students to efficiently manage and access academic records and grades.

---

## 🔐 For Admins:
- Manage student records (Add / Remove Students)  
- Manage teacher records (Add / Remove Teachers)  
- Access detailed student reports (grades, courses)  
- Search students by ID or name  
- Secure logout functionality  

---

## 👨‍🏫 For Teachers:
- Assign courses to students  
- Add/update grades for assigned courses  
- View list of students under their supervision  
- Secure logout functionality  

---

## 👨‍🎓 For Students:
- View personal grade reports  
- View enrolled courses  

---

## ⚙️ General Features:
- Role-based user authentication (Admin, Teacher, Student)  
- Intuitive and responsive Tkinter GUI  
- Data stored and managed via CSV files or Pandas DataFrames  
- Input validation and error handling  

---

## 🗂️ Project Structure

- `sgs.py`  
  Core backend logic for managing students, teachers, courses, and grades.

- `sgs_ui.py`  
  Tkinter-based frontend interfacing with the `sgs` module.

- `data/` *(optional)*  
  Directory containing CSV files used to store user, grade, and course data.

---
