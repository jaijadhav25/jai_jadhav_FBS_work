### Enter number of students from user. For those many students accept marks of 5
#   subject marks from user and calculate percentage. Display all percentage and
#   average percentage of students.

student = int(input("Enter the number of student:"))
average = 0
for i in range(1,student + 1):
    print(f"Student detiales :{i}.")
    marks = 0

    for j in range(1,6):
        subject = int(input(f"Enter the marks of subject {j}:"))
        marks = marks + subject
    
    percentage = (marks / 500)*100
    print(f"Percentage of student {i} is {percentage}.")
    average = average + percentage

average_percentage = average / student

print(f"Average percentage of student is {average_percentage}.")
