### Write a program to print first n prime numberts

num1 = int(input("Enter the number to print first n prime number:"))
count = 0
num = 2
while(count < num1):
        for i in range(2,num//2 + 1):
                 if(num % i == 0):
                       break
        else:
            print(num)
            count += 1
        num +=1
       
    
        
    