### Write a program to accept an integer amount from user and tell minimumnumber of notes needed for representing that amount.

a = int(input("Enter the Amount"))

temp = a

n1 = temp // 2000
temp = temp % 2000

n2 = temp // 500
temp = temp % 500

n3 = temp // 200
temp = temp % 200

n4 = temp // 100
temp = temp % 100

n5 = temp // 50
temp = temp % 50

n6 = temp // 20
temp = temp % 20

n7 = temp // 10
temp = temp % 10

print(f"Amount of note will be 2000:{n1}, 500:{n2}, 200:{n3}, 100:{n4}, 50:{n5}, 20:{n6}, 10:{n7} ")
print("Total amount of note will be",n1+n2+n3+n4+n5+n6+n7)