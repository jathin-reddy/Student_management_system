students = []

try:
    with open("students.txt","r") as file:
        for line in file:
            name, age, branch = line.strip().split(",") 
            student = {
                "name" : name,
                "age" : int(age),
                "branch" : branch
            }
            students.append(student)

except FileNotFoundError:
       pass