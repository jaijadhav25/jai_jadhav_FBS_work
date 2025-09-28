# 13 . Write a program to print list after removing even numbers.

def removing_even(li):
    new_list = []
    for i in range(len(li)):
        if(li[i] % 2 != 0):
            new_list.append(li[i])
    print("After removing even number:",new_list)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Orignal list:",li)
removing_even(li)