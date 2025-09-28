### Write a program to calculate the percentage of student based on marks of any 5 subject

m1 = int(input("Enter the marks of subject 1:"))
m2 = int(input("Enter the marks of subject 2:"))
m3 = int(input("Enter the marks of subject 3:"))
m4 = int(input("Enter the marks of subject 4:"))
m5 = int(input("Enter the marks of subject 5:"))

per = ((m1+m2+m3+m4+m5)/500)*100

print(f"percentage of student is {per}")