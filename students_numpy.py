import numpy as np
import pandas as pd


names = np.array(["Ravi", "Sita", "Arun", "Priya"])
marks = np.array([85, 90, 78, 88])


data = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(data)


data.to_csv("students.txt", sep="\t", index=False)

print("\nText file 'students.txt' created successfully!")