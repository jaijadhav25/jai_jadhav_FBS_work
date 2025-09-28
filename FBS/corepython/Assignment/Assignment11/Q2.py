# 2. Python Program to Merge Two Lists and Sort it

def sort(li):
    for i in range(len(li)):
        ind = i
        for j in range(i + 1, len(li)):
            if(li[j] < li[ind]):
                ind = j
        li[i], li[ind] = li[ind], li[i]
    return li        


def merge_list(li1, li2):
    print("list 1 :",li1)
    print("list 2 :",li2)
    merge_list = li1 + li2
    res = sort(merge_list)
    print("After merging list 1 and 2 is:",res)


li1 = [3, 5, 1, 4, 2]
li2 = [10, 7, 6, 9, 8]
merge_list(li1, li2)
