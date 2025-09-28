### Write a program to prompt user to enter userid and password. If Id and
#   password is incorrect give him chance to re-enter the credentials. Let
#   him try 3 times. After that program to terminate.

print("creat your user id and password!!!!!")
id = input("Enter your name for user id:")
password = int(input("Enter number for passsword:"))
print("User id and password is created:")

count = 0
while(count < 3):
    id_check = input("Enter the user id:")
    password_check = int(input("Enter the password:"))
    if(id_check == id):
        if(password_check == password):
            print("Login successfully.")
            break
        else:
            print("Incorrect password.")
            print("Please try again.")
    else:
        print("Incorrect user id.")
        print("Please try again.")
    count += 1
        