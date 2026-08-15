students = []

try:
    with open("students.txt","r") as file:
        for line in file:
            name = line.strip().split(",")[0]
            age = line.strip().split(",")[1]
            branch = line.strip().split(",")[2]
            student = {
                "name" : name,
                "age" : int(age),
                "branch" : branch
            }
            students.append(student)

except FileNotFoundError:
       pass