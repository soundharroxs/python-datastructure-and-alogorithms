"""
# @Name    :program_three.py
# @Author  :soundhar.B
# @Since   :15 Febuary 2021
# @Version :1.0
# @see     :program to accpet number  1 to 10 and print in alpabet.


"""

#declaing the dictionary
number_dict = {
    1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"
}
#getting the user input 
input_num = int(input("enter the number 1 to 10 "))

#loop through the dictinoary if number presnt print the value

print(" {} in words is".format(input_num),number_dict.get(input_num,"no a vaild number"))
