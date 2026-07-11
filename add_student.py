from database import students

def add_student():
    name = input("Enter student name:")
    age = int(input("Enter age:"))
    branch = input("Enter branch:")
    
    student = {
            "name" : name,
            "age" : age,
            "branch": branch
    }
    
    students.append(student)
    with open("students.txt", "a") as file:
        file.write(f"{name}, {age}, {branch}\n")
    print("Student data added successfully.")