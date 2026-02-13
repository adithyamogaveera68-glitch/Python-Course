import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = np.array(["Ravi", "Sita", "Arun", "Priya", "Kiran"])
marks = np.array([85, 92, 78, 88, 95])


data = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("\nStudent Data:\n", data)

min_marks = np.min(marks)
max_marks = np.max(marks)

min_student = data[data["Marks"] == min_marks]["Name"].values[0]
max_student = data[data["Marks"] == max_marks]["Name"].values[0]

print("\nMinimum Marks:", min_marks, "by", min_student)
print("Maximum Marks:", max_marks, "by", max_student)


data.to_csv("students.txt", sep="\t", index=False)


colors = []

for m in marks:
    if m == max_marks:
        colors.append("green")     
    elif m == min_marks:
        colors.append("red")       
    else:
        colors.append("skyblue")   

plt.figure()
plt.bar(names, marks, color=colors)

plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")


for i in range(len(marks)):
    plt.text(i, marks[i] + 1, str(marks[i]), ha='center')

plt.show()