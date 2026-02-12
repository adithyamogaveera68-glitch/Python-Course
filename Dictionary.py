
# dictionary 
student={
    "name":"Harsha",
    "age":20,
    "location":"Bengaluru"
}

print(student)

# Create a dictionary
student = {}

# Taking input
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student[name] = marks   # storing in dictionary

# Display dictionary
print("Student Details:")
for key in student:
    print(key, ":", student[key])

