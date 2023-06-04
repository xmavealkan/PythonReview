grade = int(input("What grade did you get? "))

if grade == 100 and grade >= 90:
    print("Your grade is: A")
elif grade < 90 and grade >= 70: 
    print("Your grade is: B")
elif grade < 70 and grade >= 50:
    print("Your grade is: C")
elif grade < 50 and grade >= 30:
    print("Your grade is: D")
elif grade < 30 and grade >= 10:
    print("Your grade is: E")
else :
    print("You failed task, your grade: F")