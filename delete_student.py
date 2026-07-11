from database import students

def delete_student():
    name = input("Enter student name:")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"Student named '{name}' deleted successfully.")
            return
    print("Student not found.")