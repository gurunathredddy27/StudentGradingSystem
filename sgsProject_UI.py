'''
The sgs_ui.py script serves as the Graphical User Interface (GUI)for the
Student Grading System (SGS).It provides an interactive interface using Tkinter
for admins and teachers to manage students, courses, and grades.

It communicates with sgs.py (the backend) to process user actions.
tkinter- is used to create the GUI
messagebox- provides pop-up messages
simpledialog allows user input dialog boxes

'''

import tkinter as tk
from tkinter import messagebox, simpledialog
import sgs  # Importing the SGS module

# Create an instance of StudentGradingSystem
sgs_system = sgs.StudentGradingSystem()

def input_dialog(title, prompt):
    return simpledialog.askstring(title, prompt)

def formatted_dict_display(data):
    return "\n".join(f"{key}: {value}" for key, value in data.items())

#Function to handle login credentials
def login():
    user_type, username, password = user_type_var.get(), username_entry.get(), password_entry.get()
    if (user_type == "admin" and sgs_system.authenticate_admin(username, password)) or \
       (user_type == "teacher" and sgs_system.authenticate_teacher(username, password)):
        messagebox.showinfo("Login Successful", f"Welcome {user_type.capitalize()}!")
        root.withdraw()
        open_dashboard(user_type, username)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

#Function to handle logout and return to login screen
def logout(window):
    window.destroy()
    root.deiconify()

#Function to open the respective panel after
def open_dashboard(user_type, user_id):
    window = tk.Toplevel(root)
    window.title(f"{user_type.capitalize()} Dashboard")
    if user_type == "admin":
        window.geometry("410x430")
    else:
        window.geometry("410x250") 
    #window.geometry("410x430")  
    window.configure(bg="white")

    main_frame = tk.Frame(window, bg="white")
    main_frame.pack(pady=10, padx=10, fill='both', expand=True)

    actions = []
    if user_type == "admin":
        actions = [
            ("Add Student", add_student),
            ("Remove Student", remove_student),
            ("Assign Course to Student", assign_course_to_student),
            ("Add Teacher", add_teacher),
            ("Remove Teacher", remove_teacher),
            ("View Teachers", view_teachers),
            ("View Student Report", view_student_report),
            ("View Students", view_students),
            ("Search Student", search_student),
            ("View Student Average", view_student_average),
            ("Predict Student Performance", predict_student_performance),
            ("Plot Student Performance", plot_student_performance),
            ("Add Course", add_course),
            ("Remove Course", remove_course)
        ]
    elif user_type == "teacher":
        actions = [
            ("Add Grade to Student", assign_grade),
            ("View Students", view_students),
            ("View Student Average", view_student_average),
            ("Predict Student Performance", predict_student_performance),
            ("Plot Student Performance", plot_student_performance)
        ]
    # Create buttons for each functionality
    for index, (text, command) in enumerate(actions):
        row, col = divmod(index, 2)  
        tk.Button(main_frame, text=text, command=command, width=25, pady=5).grid(row=row, column=col, padx=5, pady=5)
    
    tk.Button(window, text="Logout", command=lambda: logout(window), bg="#FF6666", fg="white", width=25).pack(pady=10)

#Admin and Teacher functionalities
def add_student():
    sid = input_dialog("Add Student", "Enter Student ID:")
    name = input_dialog("Add Student", "Enter Student Name:")
    age = input_dialog("Add Student", "Enter Student Age:")
    if sid and name and age:
        messagebox.showinfo("Result", sgs_system.add_student(sid, name, int(age)))

def remove_student():
    sid = input_dialog("Remove Student", "Enter Student ID:")
    if sid:
        messagebox.showinfo("Result", sgs_system.remove_student(sid))

def add_teacher():
    tid = input_dialog("Add Teacher", "Enter Teacher ID:")
    name = input_dialog("Add Teacher", "Enter Teacher Name:")
    pwd = input_dialog("Add Teacher", "Enter Password:")
    course = input_dialog("Add Teacher", "Enter Course Name:")
    if tid and name and pwd and course:
        messagebox.showinfo("Result", sgs_system.add_teacher(tid, name, pwd, course))

def remove_teacher():
    tid = input_dialog("Remove Teacher", "Enter Teacher ID:")
    if tid:
        messagebox.showinfo("Result", sgs_system.remove_teacher(tid))

def assign_course_to_student():
    sid = input_dialog("Assign Course", "Enter Student ID:")
    course = input_dialog("Assign Course", "Enter Course Name:")
    if sid and course:
        messagebox.showinfo("Result", sgs_system.assign_course_to_student(sid, course))

def view_student_report():
    sid = input_dialog("View Report", "Enter Student ID:")
    if sid:
        report_df = sgs_system.view_student_report(sid)
        if isinstance(report_df, str):  # If it's an error message
            messagebox.showerror("Error", report_df)
        else:
            messagebox.showinfo("Student Report", report_df.to_string(index=False))

def search_student():
    sid = input_dialog("Search Student", "Enter Student ID:")
    if sid:
        student_info = sgs_system.search_student(sid)
        messagebox.showinfo("Student Info", formatted_dict_display(student_info))

 
def view_teachers():
    df = sgs_system.view_teachers()
    messagebox.showinfo("Teachers List", df.to_string(index=False))

def view_students():
    df = sgs_system.view_students()
    messagebox.showinfo("Students List", df.to_string(index=False))

def assign_grade():
    sid = input_dialog("Assign Grade", "Enter Student ID:")
    course = input_dialog("Assign Grade", "Enter Course Name:")
    grade = input_dialog("Assign Grade", "Enter Grade:")
    if sid and course and grade:
        messagebox.showinfo("Result", sgs_system.assign_grades("teacher", sid, course, float(grade)))

def view_student_average():
    sid = input_dialog("View Student Average", "Enter Student ID:")
    if sid:
        avg = sgs_system.calculate_student_average(sid)
        if avg is None or isinstance(avg, str):  # Handle invalid student or errors
            messagebox.showerror("Error", avg if isinstance(avg, str) else f"Student with ID {sid} not found.")
        else:
            messagebox.showinfo("Student Average", f"Average Grade: {avg:.2f}")

#predict the student performance
def predict_student_performance():
    sid = input_dialog("Predict Performance", "Enter Student ID:")
    if sid:
        messagebox.showinfo("Performance Prediction", formatted_dict_display(sgs_system.predict_student_performance(sid)))
#ploting for the student performance is done here
def plot_student_performance():
    sid = input_dialog("Plot Performance", "Enter Student ID:")
    if sid:
        sgs_system.plot_student_performance(sid)

def add_course():
    course_name = input_dialog("Add Course", "Enter Course Name:")
    if course_name:
        messagebox.showinfo("Result", sgs_system.add_course(course_name))

def remove_course():
    course_name = input_dialog("Remove Course", "Enter Course Name:")
    if course_name:
        messagebox.showinfo("Result", sgs_system.remove_course(course_name))

#Login UI Setup
root = tk.Tk()
root.title("Student Grading System Login")
root.geometry("450x350")

frame = tk.Frame(root, bg='white')
frame.pack(pady=20)

#User type selection
tk.Label(frame, text="User Type:").grid(row=0, column=0)
user_type_var = tk.StringVar(value="admin")
tk.OptionMenu(frame, user_type_var, "admin", "teacher").grid(row=0, column=1)

#Username entry
tk.Label(frame, text="Username:").grid(row=1, column=0)
username_entry = tk.Entry(frame)
username_entry.grid(row=1, column=1)

#Password entry
tk.Label(frame, text="Password:").grid(row=2, column=0)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=2, column=1)

#Login button
tk.Button(root, text="Login", command=login).pack()

#keeps the GUI running
root.mainloop()
