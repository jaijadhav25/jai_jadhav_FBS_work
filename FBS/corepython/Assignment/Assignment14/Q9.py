# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def three_sum(li, target):
    result = []
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            for k in range(j + 1, len(li)):
                if(li[i] + li[j] + li[k] == target):
                    triplet = [li[i], li[j], li[k]] 
                
                    for a in range(2):
                        for b in range(2-a):
                            if triplet[b] > triplet[b + 1]:
                                triplet[b], triplet[b + 1] = triplet[b + 1], triplet[b]
                    
                    found = False
                    for e in result:
                        if e == triplet:
                            found = True
                            break

                    if not found:
                        result.append(triplet)
    return result

li = [1,2,3,4,5,6]
target = int(input("Enter target number:"))
print("Unique triplets:",three_sum(li, target))