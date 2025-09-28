# 10. Write a program to remove all occurrences of a given element in the list.

def remove_occurance(li):
    a = int(input("Enter number to remove occurance:"))
    new_list = []
    for i in range(len(li)):
        if(li[i] != a):
            new_list.append(li[i])
    print(f"After removing occurance of {a} is : {new_list}")
    

li = [50, 20, 30, 78, 40, 80, 10, 58, 60, 50, 80]
print("Orignal list:",li)
remove_occurance(li)