def check_password(password = ""):

    if len(password) < 10:
        return False
    

    upper_case = 0
    for char in password:
        if char.isupper():
            upper_case += 1
    
    if upper_case < 1:
        return False
    

    is_digit = 0
    for char in password:
        if char.isdigit():
            is_digit += 1
    
    if is_digit < 2 or is_digit > 3:
        return False
    

    if password.isalnum():
        return False
    
    return True

def check_student_number(student_number):
    if student_number.isdigit() and int(student_number) >= 1 and int(student_number) <= 50:
        return True
    else:
        return False

def define_student_school(student_gpa):
    if 90 <= student_gpa <= 100:
        return "School of Engineering"
    elif 80 <= student_gpa < 90:
        return "School of Business"
    elif 70 <= student_gpa < 80:
        return "Law School"
    else:
        return "Not accepted"