from add_student import add_student
from view_students import view_students
from search_student import search_student
from delete_student import delete_student

while True:
    print("\n\t\t\t\t\t======================================= Student management system ======================================= \n")
    print("1. add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter any choice:")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you for using the Student Management System.")
        break
    else:
        print("Invalid choice given!")