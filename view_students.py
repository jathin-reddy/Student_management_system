from database import students

def view_students():
    if len(students) == 0:
        print("\nNo student found!")
    else:
        print("\nDisplaying students records: \n")
    
    for student in students:
        print(student)