import json
import os
import tkinter as tk



class Student:
    count = 0
    total_grades = 0
    students = []


    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1
        Student.total_grades += grade
        Student.students.append(self)


    def get_info(self):
        return f"Name: {self.name} | Grade: {self.grade}"

    @classmethod
    def get_raw_data(cls):
        return [{"name": stud.name, "grade": stud.grade} for stud in cls.students]

    @classmethod
    def get_count(cls):
        return f"{cls.count}"

    @classmethod
    def get_total_grades(cls):
        if cls.count == 0:
            return 0
        return cls.total_grades / cls.count

    @classmethod
    def get_list(cls):
        return [stud.get_info() for stud in cls.students]

def save_data_to_file():
    data_to_save = Student.get_raw_data()
    with open("students.json", "w") as file:
        json.dump(data_to_save, file, indent=4)


def load_data_from_file():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            saved_students = json.load(file)
            for stud_dict in saved_students:
                Student(stud_dict["name"], stud_dict["grade"])


print(" === HOMEROOM STUDENTS GRADES === ")




def click_add_button():
    try:
        raw_name = name_entry.get()
        raw_grade = grade_entry.get()

        cleaned_name = raw_name.strip().title()
        validated_grade = int(raw_grade)

        current_student = Student(cleaned_name, validated_grade)

        save_data_to_file()

        student_listbox.delete(0, tk.END)
        student1_listbox.delete(0, tk.END)
        student2_listbox.delete(0, tk.END)


        total_students = Student.get_count()
        student2_listbox.insert(tk.END, total_students)

        total_grade = Student.get_total_grades()
        student1_listbox.insert(tk.END, total_grade)

        for student_info in Student.get_list():
            student_listbox.insert(tk.END, student_info)

        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)




    except ValueError:
        print("Invalid! Grade must be a number.")


root = tk.Tk()
root.title("Homeroom Grades App")
root.geometry("500x450")  #

name_label = tk.Label(root, text="Student Name:")
name_label.grid(row=0, column=1, padx=140, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=140, pady=5)

# 3. Row 1: Grade Label and Entry Box
grade_label = tk.Label(root, text="Average Grade:")
grade_label.grid(row=2, column=1, padx=140, pady=5)

grade_entry = tk.Entry(root)
grade_entry.grid(row=3, column=1, padx=140, pady=5)

add_button = tk.Button(root, text="Add Student", command=click_add_button)
add_button.grid(row=4, column=1, padx=140, pady=5)

student_listbox = tk.Listbox(root, width=40, height=5)
student_listbox.grid(row=5, column=1, padx=140, pady=5)

student1_label = tk.Label(root, text="Total AVG Grade")
student1_label.grid(row=6, column=1, padx=140, pady=5)


student1_listbox = tk.Listbox(root, width=28, height=1)
student1_listbox.grid(row=7, column=1, padx=140, pady=0)

student2_label = tk.Label(root, text="Number of Students")
student2_label.grid(row=8, column=1, padx=140, pady=5)


student2_listbox = tk.Listbox(root, width=28, height=1)
student2_listbox.grid(row=9, column=1, padx=140, pady=0)

load_data_from_file()

student_listbox.delete(0, tk.END)
student1_listbox.delete(0, tk.END)
student2_listbox.delete(0, tk.END)

total_students = Student.get_count()
student2_listbox.insert(tk.END, total_students)

total_grade = Student.get_total_grades()
student1_listbox.insert(tk.END, total_grade)

for student_info in Student.get_list():
    student_listbox.insert(tk.END, student_info)


root.mainloop()







