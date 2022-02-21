"""
# @Name    : program_seventeen.py
# @Author  :soundhar.B
# @Since   : 18 Febuary 2021
# @Version :1.0
# @see     :  program to reverse a string.

"""
#get a input from the user
simple_string = input("Enter the string : ")
reverse = ""
#loop the string and store it.
for lp in simple_string :
    reverse=lp+reverse

print("reverse of string" ,reverse)