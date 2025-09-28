### Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random

print("Create userid and passward")
user_id_creation = input("Enter your name for userid:")
password_creation = int(input("Enter number for password:"))
print("User id and passward is created.")
captcha = random.randint(1111,9999)

user_id_login = input("Enter the user id:")
password_login = int(input("Enter the password:"))
print(captcha)
captcha_type = int(input("Enter the captcha:"))

if(user_id_login == user_id_creation):
    if(password_login == password_creation):
        if(captcha_type == captcha):
            print("Successfully login:")
        else:
            print("captcha is incorrect.")
    else:
        print("password is incorrect.")
else:
    print("user id is incorrect.")