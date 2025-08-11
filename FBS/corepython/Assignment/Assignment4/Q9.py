### WAP to print all numbers in a range divisible by a given number.
start_num = int(input("Enter the starting number:"))
end_num = int(input("Enter the ending number:"))

num = int(input("Enter the number to divide:"))

for i in range(start_num, end_num +1):
    if(i % num == 0):
        print(i,end=",")