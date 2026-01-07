1) Use a dictionary to build a table
import pandas as pd

class_record = {
    'Student_Name': ['Arjun', 'Sanya', 'Vikram', 'Ananya', 'Rahul'],
    'Math': [85, 92, 78, 88, 95],
    'Science': [90, 85, 80, 92, 89]
}

gradebook = pd.DataFrame(class_record)
print("Class Grades:")
print(gradebook)

2) Counting Missing Data
# missing values (None)
attendance = {'Day': [1, 2, 3, 4, 5], 'Number_of_student': [30, None, 28, None, 31]}
df_attendance = pd.DataFrame(attendance)

empty_check = df_attendance.isnull().sum()
print("Count of missing data per column:")
print(empty_check)

3) Selecting Feature of our need

personal_info = pd.DataFrame({
    'Name : ['Alice', 'Bob'],
    'Age': [25, 30],
    'Favorite_Color': ['Blue', 'Red'],
    'Height_cm': [165, 180],
})

essential_columns = ['Name', 'Height_cm']
filtered_data = personal_info[essential_columns]

print("Filtered Information:")
print(filtered_data)

4) Filtering Data

Nerds = grade[grade['Math'] > 90]
print("Students who scored above 90 in Math:")
print(Nerds)

