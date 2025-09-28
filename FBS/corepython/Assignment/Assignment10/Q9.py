# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.


def seperate_even_odd(li):
    even = []
    odd = []
    for i in range(len(li)):
        if(li[i] % 2 == 0):
            even.append(li[i])
        else:
            odd.append(li[i])
    print("Even list",even)
    print("Odd list",odd)

n = int(input("Enter the length of list."))
li = []
for i in range(n):
    ele = int(input("Enter the element:"))
    li.append(ele)

print("Orignal list :",li)
seperate_even_odd(li)


