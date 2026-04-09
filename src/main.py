import tkinter
from extras import check_password, check_student_number, define_student_school

password_tries = 0
student_number_tries = 0
student_quantity = 0
student_name_list = []
student_grade_list = []
student_gpa_list = []
student_accepted_school_list = []

def password_get():
    global password_tries
    
    password = password_entry.get()
    
    if check_password(password):
        print("Password is valid.")
        
        welcome.destroy()
        Password_label.destroy()
        password_entry.destroy()
        login_button.destroy()
        warning_password.destroy()

        student_input_window()

    else:
        password_tries += 1

        if password_tries >= 3:
            root.destroy()
            return

        print("Password is invalid.")
        warning_password.pack()

def student_number_get():
    global student_number_tries
    global student_quantity

    student_number = class_entry.get()

    if check_student_number(student_number):
        class_warning.destroy()
        print("Student number is valid.")

        class_label.destroy()
        class_entry.destroy()
        class_button.destroy()

        student_quantity = int(student_number)
        student_input_names()

    else:
        student_number_tries += 1

        if student_number_tries >= 3:
            root.destroy()
            return

        print("Student number is invalid.")
        class_warning.pack()

def student_name_get():
    student_name = student_name_entry.get()


    if len(student_name.split()) == 2:
        student_name_list.append(student_name)

        student_name_entry.delete(0, tkinter.END)

        student_name_info_label.config(text=f"Student {len(student_name_list)} added: {student_name}")

        student_name_info_label.pack()

        student_name_warning.pack_forget()
    else:
        student_name_info_label.pack_forget()

        student_name_warning.pack()

    if len(student_name_list) >= student_quantity:
        student_name_label.destroy()
        student_name_description.destroy()
        student_name_entry.destroy()
        student_name_button.destroy()
        student_name_info_label.destroy()
        student_name_warning.destroy()

        student_input_grades()
            
def student_grade_get():
    math_grade = student_grades_math_entry.get()
    science_grade = student_grades_science_entry.get()
    language_grade = student_grades_language_entry.get()
    drama_grade = student_grades_drama_entry.get()
    music_grade = student_grades_music_entry.get()
    biology_grade = student_grades_biology_entry.get()
    
    if (math_grade.isdigit() and 0 <= int(math_grade) <= 100 and
        science_grade.isdigit() and 0 <= int(science_grade) <= 100 and
        language_grade.isdigit() and 0 <= int(language_grade) <= 100 and
        drama_grade.isdigit() and 0 <= int(drama_grade) <= 100 and
        music_grade.isdigit() and 0 <= int(music_grade) <= 100 and
        biology_grade.isdigit() and 0 <= int(biology_grade) <= 100):
        
        student_grades_warning.pack_forget()

        student_grades = [
            [int(math_grade), 4],
            [int(science_grade), 5],
            [int(language_grade), 4],
            [int(drama_grade), 3],
            [int(music_grade), 2],
            [int(biology_grade), 4]
        ]

        student_grade_list.append(student_grades)

        student_grades_math_entry.delete(0, tkinter.END)
        student_grades_science_entry.delete(0, tkinter.END)
        student_grades_language_entry.delete(0, tkinter.END)
        student_grades_drama_entry.delete(0, tkinter.END)
        student_grades_music_entry.delete(0, tkinter.END)
        student_grades_biology_entry.delete(0, tkinter.END)

        student_grades_info_label.config(text=f"Grades for {student_name_list[len(student_grade_list) - 1]} added.")
        student_grades_info_label.pack()
    else:
        student_grades_info_label.pack_forget()
        student_grades_warning.pack()

    if len(student_grade_list) >= student_quantity:
        student_grades_label.destroy()
        student_grades_description.destroy()
        student_grades_math_label.destroy()
        student_grades_math_entry.destroy()
        student_grades_science_label.destroy()
        student_grades_science_entry.destroy()
        student_grades_language_label.destroy()
        student_grades_language_entry.destroy()
        student_grades_drama_label.destroy()
        student_grades_drama_entry.destroy()
        student_grades_music_label.destroy()
        student_grades_music_entry.destroy()
        student_grades_biology_label.destroy()
        student_grades_biology_entry.destroy()
        student_grades_button.destroy()
        student_grades_info_label.destroy()
        student_grades_warning.destroy()

        for student_grade in student_grade_list:
            gpa_marks = 0
            total_credits = 0
            for grade in student_grade:
                gpa_marks += (grade[0] / 100) * grade[1]
                total_credits += grade[1]
            
            student_gpa_list.append((gpa_marks / total_credits) * 100)
            student_accepted_school_list.append(define_student_school((gpa_marks / total_credits) * 100))

        student_report()

def print_report1():
    
    append_string = ""

    append_string += """=================================
Report 1: Student Names and Accepted Schools
=================================
"""

    for i in range(student_quantity):
        print(f"Student: {student_name_list[i]}")
        append_string += f"Student: {student_name_list[i]} \n"
        print(f"Accepted School: {student_accepted_school_list[i]}")
        append_string += f"Accepted School: {student_accepted_school_list[i]}\n"
        print("")
        append_string += "========================\n"

    with open("output/report1.txt", "w") as report_file:
        report_file.write(append_string)

def print_report2():
    accepted_students = 0
    engineering_students = 0
    business_students = 0
    law_students = 0

    append_string = ""

    append_string += """=================================
Report 1: Total accepted students and accepted students in each school
=================================
"""

    for i in student_accepted_school_list:
        accepted_students += 1 if i != "Not accepted" else 0

        if i == "School of Engineering":
            engineering_students += 1
        elif i == "School of Business":
            business_students += 1
        elif i == "Law School":
            law_students += 1
    
    print(f"Total accepted students: {accepted_students}")
    append_string += f"Total accepted students: {accepted_students}\n"
    print(f"Total students accepted in the School of Engineering: {engineering_students}")
    append_string += f"Total students accepted in the School of Engineering: {engineering_students}\n"
    print(f"Total students accepted in the School of Business: {business_students}")
    append_string += f"Total students accepted in the School of Business: {business_students}\n"
    print(f"Total students accepted in the Law School: {law_students}")
    append_string += f"Total students accepted in the Law School: {law_students}\n"

    with open("output/report2.txt", "w") as report_file:
        report_file.write(append_string)

def print_report3():
    not_accepted_students = 0
    for i in student_accepted_school_list:
        not_accepted_students += 1 if i == "Not accepted" else 0
    print(f"Total of not accepted students: {not_accepted_students}")
    with open("output/report3.txt", "w") as report_file:
        report_file.write(f"""==================================
Report 3: Total not accepted students
==================================
Total of not accepted students: {not_accepted_students}\n""")

def print_report4():
    mean_engineering_gpa = 0
    mean_business_gpa = 0
    mean_law_gpa = 0

    append_string = ""

    append_string += """=================================
Report 4: Mean GPA of accepted students in each school
=================================
"""

    for i in student_accepted_school_list:
        if i == "School of Engineering":
            mean_engineering_gpa += student_gpa_list[student_accepted_school_list.index(i)]
        elif i == "School of Business":
            mean_business_gpa += student_gpa_list[student_accepted_school_list.index(i)]
        elif i == "Law School":
            mean_law_gpa += student_gpa_list[student_accepted_school_list.index(i)]
        
    mean_engineering_gpa /= student_accepted_school_list.count("School of Engineering")
    mean_business_gpa /= student_accepted_school_list.count("School of Business")
    mean_law_gpa /= student_accepted_school_list.count("Law School")

    print(f"Mean GPA of students accepted in the School of Engineering: {mean_engineering_gpa:.2f}")
    append_string += f"Mean GPA of students accepted in the School of Engineering: {mean_engineering_gpa:.2f}\n"
    print(f"Mean GPA of students accepted in the School of Business: {mean_business_gpa:.2f}")
    append_string += f"Mean GPA of students accepted in the School of Business: {mean_business_gpa:.2f}\n"
    print(f"Mean GPA of students accepted in the Law School: {mean_law_gpa:.2f}")
    append_string += f"Mean GPA of students accepted in the Law School: {mean_law_gpa:.2f}\n"

    with open("output/report4.txt", "w") as report_file:
        report_file.write(append_string)

root = tkinter.Tk()
root.title("Humber College Login")
root.geometry("300x200")
welcome = tkinter.Label(root, text="Welcome in Humber College!")

welcome.pack()


Password_label = tkinter.Label(root, text="Please enter your password.")
Password_label.pack()

warning_password = tkinter.Label(root, text="Your password does not meet the requirements.")

password_entry = tkinter.Entry(root, show="*")
password_entry.pack()

login_button = tkinter.Button(root, text="Login", command=password_get)
login_button.pack()

class_label = tkinter.Label(root, text="Please input the number of students in the class.")
class_entry = tkinter.Entry(root)
class_warning = tkinter.Label(root, text="Please enter a valid student number between 1 and 50.")
class_button = tkinter.Button(root, text="Submit", command=student_number_get)

student_name_label = tkinter.Label(root, text="Please input the name of the student.")
student_name_description = tkinter.Label(root, text='The name should be in the format: "Firstname Lastname".\nFor each student, input their name and press the "Submit" button.',
                                         wraplength=400)
student_name_entry = tkinter.Entry(root)
student_name_info_label = tkinter.Label(root, text="")
student_name_warning = tkinter.Label(root, text="Please enter a valid name in the format 'Firstname Lastname'.")
student_name_button = tkinter.Button(root, text="Submit", command=student_name_get)

student_grades_label = tkinter.Label(root, text="Please input the grades of the students.")
student_grades_description = tkinter.Label(root, text='The grade should be a number between 0 and 100.\nFor each student, input their grades and press the "Submit" button.\n',
                                         wraplength=400)

student_grades_math_label = tkinter.Label(root, text="Math:")
student_grades_math_entry = tkinter.Entry(root)
student_grades_science_label = tkinter.Label(root, text="Science:")
student_grades_science_entry = tkinter.Entry(root)
student_grades_language_label = tkinter.Label(root, text="Language:")
student_grades_language_entry = tkinter.Entry(root)
student_grades_drama_label = tkinter.Label(root, text="Drama:")
student_grades_drama_entry = tkinter.Entry(root)
student_grades_music_label = tkinter.Label(root, text="Music:")
student_grades_music_entry = tkinter.Entry(root)
student_grades_biology_label = tkinter.Label(root, text="Biology:")
student_grades_biology_entry = tkinter.Entry(root)

student_grades_info_label = tkinter.Label(root, text="")
student_grades_warning = tkinter.Label(root, text="Please enter a valid grade between 0 and 100.")
student_grades_button = tkinter.Button(root, text="Submit", command=student_grade_get)

student_print_report_button = tkinter.Button(root, text="Print Report 1", command=print_report1)
student_print_report_button2 = tkinter.Button(root, text="Print Report 2", command=print_report2)
student_print_report_button3 = tkinter.Button(root, text="Print Report 3", command=print_report3)
student_print_report_button4 = tkinter.Button(root, text="Print Report 4", command=print_report4)

def student_input_window():
    root.title("Humber College Grading System")
    root.geometry("500x300")

    class_label.pack()
    class_entry.pack()
    class_button.pack()

def student_input_names():
    student_name_label.pack()
    student_name_description.pack()
    student_name_entry.pack()
    student_name_button.pack()

def student_input_grades():
    root.geometry("500x400")

    student_grades_label.pack()
    student_grades_description.pack()
    student_grades_math_label.pack()
    student_grades_math_entry.pack()
    student_grades_science_label.pack()
    student_grades_science_entry.pack()
    student_grades_language_label.pack()
    student_grades_language_entry.pack()
    student_grades_drama_label.pack()
    student_grades_drama_entry.pack()
    student_grades_music_label.pack()
    student_grades_music_entry.pack()
    student_grades_biology_label.pack()
    student_grades_biology_entry.pack()
    student_grades_button.pack()

def student_report():
    root.geometry("500x300")

    student_print_report_button.pack()
    student_print_report_button2.pack()
    student_print_report_button3.pack()
    student_print_report_button4.pack()

root.mainloop()