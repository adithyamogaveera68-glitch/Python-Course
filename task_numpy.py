import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


names = np.array(["Ravi", "Sita", "Arun", "Priya", "Kiran"])
marks = np.array([85, 92, 78, 88, 95])

data = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(data)


data.to_csv("students.txt", sep="\t", index=False)


plt.figure()
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Graph")

plt.show()