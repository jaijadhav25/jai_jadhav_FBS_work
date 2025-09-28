# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def check_key(dict):
    n = int(input("Enter the key:"))
    if n in dict:
        print("key is present.")
    else:
        print("key is not present.")

dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date"}
check_key(dict)