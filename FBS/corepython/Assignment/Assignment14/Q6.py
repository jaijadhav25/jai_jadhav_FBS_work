# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

def max_product_pair(numbers):
    num_set = set(numbers)

    li = []
    for  n in num_set:
        li.append(n)

    ## short list using selection sort
    for i in range(0, len(li)):
        ind = i
        for j in range(i+1, len(li)):
            if(li[j] < li[ind]):
                ind = j
        li[i], li[ind] = li[ind], li[i]
    print("Sorted list:",li)

    if(li[0] * li[1] > li[-2] * li[-1]):
        print(f'The Number {li[0]} and {li[1]} is product is maximum: {li[0]*li[1]}')
    else:
        print(f"The Number {li[-1]} and {li[-2]} is product of maximun:{li[-1]*li[-2]}")



number = [3, 5, -10, -20, 6, 2]
max_product_pair(number)
# li = [3,1,2,-10,-9,8,7,9,10]
# max_product_pair(li)