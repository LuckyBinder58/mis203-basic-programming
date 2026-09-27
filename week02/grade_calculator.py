students = []  #An empty container to hold student data

while True:
    #This part will stop the program if the user enters 'q' for the name
    name = input("Enter student name (or q to quit): ")
    if name == "q":
        break

    #Ask for the user's score
    score = float(input("Enter score: "))

    #Full range of scores that can be entered
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue  
    
    #Display the grade based on the score
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    #Display the result for the current user
    print(f"{name}: {int(score)} -> {grade}")

    #Store the entry for later (summary stats + CSV export)
    students.append((name, score, grade))

#Summary of user
if students:
    total = len(students)
    average = round(sum(s[1] for s in students) / total, 2)
    print(f"Total students: {total}")
    print(f"Average score: {average}")

    #The same feature that i implemented in previous assignment when program creates .csv file with the results of the user
    import csv
    import os

    sorted_students = sorted(students, key=lambda s: s[0])

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop, "Results.csv")
    file_exists = os.path.isfile(filepath)

    with open(filepath, "a", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")

        if not file_exists:
            writer.writerow(["Name", "Score", "Grade"])

        for name, score, grade in sorted_students:
            writer.writerow([name, score, grade])

    print(f"Results saved to {filepath}")
else:
    print("No students entered.")

#User must write "q" to quit the program and create a .csv file with the results of the user