'''
The sgs.py scripts has Student Grading System which allows teachers to record and manage student grades.
The system will support multiple functionalities such as adding student information,
inputting grades, calculating final grades, generating grade reports, and viewing student details.

==================  ==================================================
Function                  Description
==================  ==================================================
class :                   It encapsulates data (attributes) and behaviors (methods)
add_student():            Adds a student with ID, name, and age
remove_student():         Removes a student by ID
add_teacher():            Adds a teacher with ID, name, and password
remove_teacher():         Removes a teacher by ID
verify_login():           Verifies credentials for admin and teachers
assign_course_student():  Assigns a course to a student
assign_grades():          Assigns a grade to a student for a course
view_teachers():          Display all teachers
view_students():          Display all students
view_student_report():    Retrieves student course and grade details
search_student():         Searches for a student by ID.
view_student_report():    It used to view the student report
calculate_student_average(): It calculates the student average grades
predict_student_performance(): It predicts the performance with regression techniques
plot_student_performance(): Here the grades visulaized with bar graphs
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

#Initializes the Student Grading System with admin 
class StudentGradingSystem:
    def __init__(self):
        #admin credentials
        self.admin = {"username": "admin", "password": "guru42"} 

        #Teacher with assigned courses
        self.teachers = {
            "guru": {"password": "guru42", "courses": ["Python"]},
            "guru1": {"password": "guru42", "courses": ["Data Science with Python"]},
            "guru2": {"password": "guru42", "courses": ["Machine Learning"]},
            "guru3": {"password": "guru42", "courses": ["Deep Learning with TensorFlow"]},
            "guru4": {"password": "guru42", "courses": ["Advanced Python"]},
            "guru5": {"password": "guru42", "courses": ["NLP"]}
        }

        #Dictionary of student with courses and their grades
        self.students = {
            "101": {"name": "Harry", "age": 20, "courses": {"Python": 90, "Data Science with Python": 89}},
            "102": {"name": "Ron", "age": 21, "courses": {"Machine Learning": 78, "Deep Learning with TensorFlow": 78}},
            "103": {"name": "Hermoine", "age": 22, "courses": {"Advanced Python": 98, "NLP": 87}},
            }

        #set of available courses
        self.courses = {"Python", "Data Science with Python", "Machine Learning", "Deep Learning with TensorFlow",
                        "Advanced Python", "NLP"}

        #Courses assigned to teachers
        self.teacher_courses = {
            "Python": "guru",
            "Data Science with Python": "guru1",
            "Machine Learning": "guru2",
            "Deep Learning with TensorFlow": "guru3",
            "Advanced Python": "guru4",
            "NLP": "guru5"
        }

    #Verifies admin login details
    def authenticate_admin(self, username, password):
        return username == self.admin["username"] and password == self.admin["password"]

    #Verifies teacher login details
    def authenticate_teacher(self, teacher_id, password):
        return teacher_id in self.teachers and self.teachers[teacher_id]["password"] == password

    #After login moves to respective user (admin or teacher)
    def verify_login(self, user_type, user_id, password):
        if user_type == "admin":
            return self.authenticate_admin(user_id, password)
        elif user_type == "teacher":
            return self.authenticate_teacher(user_id, password)
        return False

    #Adds a new teacher 
    def add_teacher(self, teacher_id, teacher_name, teacher_password, course):
        if teacher_id in self.teachers:
            return "Teacher ID already exists"
        if course in self.teacher_courses:
            return f"Error: Course '{course}' is already assigned to {self.teacher_courses[course]}"

        self.teachers[teacher_id] = {"name": teacher_name, "password": teacher_password, "courses": [course]}
        self.teacher_courses[course] = teacher_id
        return f"Teacher '{teacher_name}' added successfully and assigned to course '{course}'!"

    #Removes a teacher
    def remove_teacher(self, teacher_id):
        if teacher_id in self.teachers:
            del self.teachers[teacher_id]
            return "Teacher removed successfully"
        return "Teacher not found!"

    #Add a student
    def add_student(self, student_id, student_name, student_age):
        if student_id in self.students:
            return "Student ID already exists"

        try:
            student_age = int(student_age)
            if student_age <= 0:
                return "Error.. Age is not valid"
        except ValueError:
            return "Error.. Invalid age. Please try again"

        self.students[student_id] = {"name": student_name, "age": student_age, "courses": {}}
        return "Student added successfully"

    #Removes a student
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return "Student removed successfully!"
        return "Student not found!"

    #Assigns a course to a student.
    def assign_course_to_student(self, student_id, course):
        if student_id not in self.students:
            return "Error.. Student not found!"
        if course not in self.courses:
            return "Error.. Invalid course name!"
        if course in self.students[student_id]["courses"]:
            return "Course already assigned to the student"
        self.students[student_id]["courses"][course] = None
        return f"Course '{course}' assigned to {self.students[student_id]['name']}."

    #Assigns a grade to a student for a specific course
    def assign_grades(self, teacher_id, student_id, course, grade):
        if student_id not in self.students:
            return "Error.. Student not found!"
        if course not in self.students[student_id]["courses"]:
            return "Error.. Course not assigned to student"
        if course not in self.teachers[teacher_id]["courses"]:
            return "Error.. You cannot assign a grade for this course"

        try:
            grade = float(grade)
            if grade < 0 or grade > 100:
                return "Error.. Grade must be between 0 and 100"
        except ValueError:
            return "Error.. Invalid grade, try again"

        self.students[student_id]["courses"][course] = grade
        return f"Grade '{grade}' assigned for course '{course}' by {teacher_id}"

    #Display students
    def view_students(self):   
        return pd.DataFrame.from_dict(self.students, orient='index')

    #Display teacher
    def view_teachers(self):
        data = []
        for tid, info in self.teachers.items():
            for course in info["courses"]:
                data.append({"Teacher ID": tid, "Courses": course})
        return pd.DataFrame(data)
        #return pd.DataFrame.from_dict(self.teachers, orient='index')

    #search students with ID
    def search_student(self, student_id):
        return self.students.get(student_id, "Student not found!")

    #View student report with ID
    def view_student_report(self, student_id):
        student = self.students.get(student_id)
        if not student:
            return f"Student with ID {student_id} not found."
        data = {
            "Course": list(student["courses"].keys()),
            "Grade": list(student["courses"].values())
            }
        df = pd.DataFrame(data)
        return df

    #calculate student average with ID
    def calculate_student_average(self, student_id):
        student = self.students.get(student_id)
        if not student:
            return f"Student with ID {student_id} not found."
    
        grades = list(student["courses"].values())  # Extract grades
        if not grades:  # Check if there are no grades
            return "No grades available for this student."
    
        return sum(grades) / len(grades)  # Compute average


    #Predict student performance with ID
    def predict_student_performance(self, sid):
        student = self.students.get(sid)
        if not student:
            return "Student not found"

        data = {"Course": [], "Grade": []}
        for course, grade in student["courses"].items():
            if grade is not None:
                data["Course"].append(course)
                data["Grade"].append(grade)

        if len(data["Grade"]) < 2:
            return "Not enough data for prediction"

        df = pd.DataFrame(data)
        X = np.arange(len(df)).reshape(-1, 1)
        y = df["Grade"]

        regression_models = {
            "Linear Regression": LinearRegression(),
            "Polynomial Regression": PolynomialFeatures(degree=2),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest": RandomForestRegressor(n_estimators=100)
        }

        predictions = {}
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        for model_name, model in regression_models.items():
            if model_name == "Polynomial Regression":
                poly = PolynomialFeatures(degree=2)
                X_train_poly = poly.fit_transform(X_train)
                X_test_poly = poly.transform(X_test)
                lin_reg = LinearRegression()
                lin_reg.fit(X_train_poly, y_train)
                y_pred = lin_reg.predict(X_test_poly)
            else:
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

            predictions[model_name] = {
                "Predicted Grades": y_pred.tolist(),
                #"Mean Absolute Error": mean_absolute_error(y_test, y_pred),
                #"R2 Score": r2_score(y_test, y_pred)
            }
        return predictions

    #ploting the performance with ID
    def plot_student_performance(self, sid):
        student = self.students.get(sid)
        if not student:
            print("Student not found")
            return

        data = {"Course": [], "Grade": []}
        for course, grade in student["courses"].items():
            if grade is not None:
                data["Course"].append(course)
                data["Grade"].append(grade)

        if not data["Grade"]:
            print("No grades available for plotting")
            return

        df = pd.DataFrame(data)

        plt.figure(figsize=(8, 5))
        sns.barplot(x="Course", y="Grade", hue="Course",data=df, palette="magma")
        plt.xticks(rotation=45)
        plt.xlabel("Courses")
        plt.ylabel("Grades")
        plt.title(f"Student {sid} Performance")
        plt.ylim(0, 100)
        plt.show()

