# Student Grade Book Program (Python 3.8.1)

# List - student names
students = ["Raj", "Priya", "Amit", "Sneha", "Karan"]

# Tuple - subject names
subjects = ("Math", "Science", "English")

# Dictionary - marks of each student
marks = {
    "Raj": {"Math": 85, "Science": 78, "English": 90},
    "Priya": {"Math": 92, "Science": 88, "English": 85},
    "Amit": {"Math": 70, "Science": 75, "English": 68},
    "Sneha": {"Math": 95, "Science": 90, "English": 92},
    "Karan": {"Math": 80, "Science": 82, "English": 78}
}

# Set - unique grades
unique_grades = set()

print("All Students:", students)
print("First 3 Students:", students[:3])
print()

highest_avg = 0
top_student = ""

# Calculate averages and grades
for student in students:
    total = 0
    for sub in subjects:
        total += marks[student][sub]

    average = total / len(subjects)

    # Grading logic
    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "C"

    unique_grades.add(grade)

    print(f"{student} - Average: {average:.2f} - Grade: {grade}")

    # Find top scorer
    if average > highest_avg:
        highest_avg = average
        top_student = student

print()
print("Top Student:", top_student)
print("Unique Grades:", unique_grades)