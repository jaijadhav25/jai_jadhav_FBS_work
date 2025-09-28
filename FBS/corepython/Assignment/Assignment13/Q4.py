# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

def dict_till_n(num):
    dict = {}
    for i in range(1,num+1):
        dict[i] = i*i

    return dict

num = int(input("Enter a number :"))
res = dict_till_n(num)
print(res)
