# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def bubble_sort(li):
    for i in range(1, len(li)):
        for j in range(0,len(li) - 1):
            if(li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]
    return li

def second_largest(li):
    li.reverse()
    print(f"Second largest element is {li[1]}")

li = [60, 50, 40, 30, 20, 10]
new = bubble_sort(li)
print(new)
second_largest(new)