student_name = input("Enter the student name: ")
Maths_marks = int(input("Enter Maths marks: "))
Science_marks = int(input("Enter Science marks: "))
English_marks = int(input("Enter English marks: "))
if Maths_marks < 0 or Maths_marks > 100 or Science_marks < 0 or Science_marks > 100 or English_marks < 0 or English_marks > 100:
    print("Invalid marks entered")
else:
    total_marks = Maths_marks + Science_marks + English_marks
    percentage = total_marks / 3

    # Now all prints happen together
    print("\nStudent Name:", student_name)
    print("Total Marks:", total_marks)
    print("Percentage:", format(percentage, ".2f"))

    if Maths_marks < 40 or Science_marks < 40 or English_marks < 40:
        print("Status: FAIL")

    else:
        print("Status: PASS")

        if percentage >= 75:
            print("Grade: A")
        elif percentage >= 60:
            print("Grade: B")
        elif percentage >= 40:
            print("Grade: C")