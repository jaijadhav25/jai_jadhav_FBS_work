### Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter the alphabet:")

if( alphabet  in ('aAeEiIoOuU')):
    print("The vowel")
else:
    print("The consonant")