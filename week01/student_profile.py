import os
import csv

# Simple survey to gather students info
name = input("Enter your Full Name: ")
department = input("Enter your Department: ")
age = input("Enter your Age: ")
career_goal = input("Enter your Career Goal: ")

# Printing the info we got from students in console
print("--- Student Profile ---")
print("Full Name:", name)
print("Department:", department)
print("Age:", age)
print("Career Goal:", career_goal)

# Path to save the CSV file on the user's Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop, "student_profiles.csv")

headers = ["Full Name", "Department", "Age", "Career Goal"]

# Simple check to see if the file already exists to avoid creating duplicate headers and files on the Desktop
file_exists = os.path.exists(file_path)

# Append mode: "a" adds a new row each run instead of overwriting
with open(file_path, "a", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    if not file_exists:
        writer.writerow(headers)
    writer.writerow([name, department, age, career_goal])

print(f"\nProfile saved to: {file_path}")
