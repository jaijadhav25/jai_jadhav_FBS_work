### Write a program to check if user has entered correct userid and password.

print("Create userid and passward")
user_id_creation  = input("Enter your name for userid:")
password_creation = int(input("Enter number for password:"))
print("User id and passward is created.")

user_id_login = input("Enter the user id:")
password_login = int(input("Enter the password:"))

if(user_id_login == user_id_creation ):
    if(password_login == password_creation):
        print("Successfully login:")
    else:
        print("password is incorrect:")
else:
    print("user id is incorrect:")

#if(a == x and b == y):
#   print("Successfully login:")
#else:
#    print("incorrect user id or password:")