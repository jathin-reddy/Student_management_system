from database import students

def search_student():
    name = input("Enter student name:")
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student named '{name}' found.")
            print(student)
            return
    print("Student not found!")