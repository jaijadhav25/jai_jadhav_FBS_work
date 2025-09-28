### Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = int(input("Enter the mark of first subject:"))
sub2 = int(input("Enter the mark of second subject:"))
sub3 = int(input("Enter the mark of third subject:"))
sub4 = int(input("Enter the mark of fourth subject:"))
sub5 = int(input("Enter the mark of fifth subject:"))

total_marks = ((sub1+sub2+sub3+sub4+sub5)/500)*100
print(f"student marks is {total_marks}")
if(total_marks >= 91):
    print("Student grade :Outstanding.")
elif(total_marks >= 81):
    print("Student grade :Excellent.")
elif(total_marks >= 71):
    print("Student grade :First class.")
elif(total_marks >= 61):
    print("Student grade :Sceond class.")
elif(total_marks >= 51):
    print("Student grade :Third class.")
elif(total_marks >= 41):
    print("Student grade :Pass.")
else:
    print("Student grade :Fail.")