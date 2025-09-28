# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def count_number(li):
    num = int(input("Enter number check if it is present in list or not:"))
    count = 0
    for i in range(0 , len(li)):
        if(li[i] == num):
            count += 1
    if(count > 1):
        print(f'Number is present.')
        print(f"Number is repeated in list {count} times.")
    else:
        print("Number is not present.")

li = [50, 20, 30, 78, 40, 80, 10, 58, 60, 50, 80]
count_number(li)