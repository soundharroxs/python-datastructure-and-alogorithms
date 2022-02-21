"""
# @Name    :program_eightteen.py
# @Author  :soundhar.B
# @Since   : 19 Febuary 2021
# @Version :1.0
# @see     :  program to check if palindrome.

"""
#get a input from the user
simple_string = input("Enter the string : ")
reverse = ""
#loop the string and store it.
for lp in simple_string :
    reverse=lp+reverse

if reverse == simple_string:
    print("It is palindrome")
else :
    print("Its is not plaindrome")