📕 Student Grading System (Tkinter app)

A desktop application using Python Tkinter that enables administrators, teachers, and students to efficiently manage and access academic records and grades.

Key Features

For Admins:
• Manage student records (Add / Remove Students)
• Manage teacher records (Add / Remove Teachers)
• Access detailed student reports, including grades and enrolled courses
• Search for students by ID or name
• Secure logout functionality

For Teachers:
• Assign courses to students
• Input and update grades for assigned courses
• View list of students under their supervision
• Secure logout functionality

For Students:
• Access personal grade reports
• View enrolled courses and grades

General Features:
• Role-based user authentication (Admin, Teacher, Student)
• Intuitive and responsive Tkinter GUI
• Data stored and managed via CSV files or Pandas DataFrames
• Robust input validation and error handling 

 --- 

Project Structure

• sgs.py  
  Core backend logic and data handling (student, teacher, course, grading management).

• sgs_ui.py  
  Tkinter GUI code interfacing with the sgs module to provide a user-friendly interface.

• data/ (optional)  
  Directory containing CSV files or data storage for users, grades, and courses.
