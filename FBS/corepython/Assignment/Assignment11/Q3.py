# 3. Python Program to Sort the List According to the Second Element in Sublist

def sort_second(li):
    for i in range(len(li)):
        for j in range(0, len(li) - i - 1):
            if(li[j][1] > li[j + 1][1]):
                li[j], li[j + 1] = li[j + 1], li[j]
    return li

li = [[1, 4], [3, 2], [5, 6], [7, 1,5]]
res = sort_second(li)
print("After sorting list with second element:",res)