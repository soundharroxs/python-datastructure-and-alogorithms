"""
# @Name    :program_seven.py
# @Author  :soundhar.B
# @Since   : 15 Febuary 2021
# @Version :1.0
# @see     : program to print and  move string to list.



"""

#declaring the variable
string_ = input("Emter the number : ")
simple_list = []

#appending to the string
for num in string_:
    simple_list.append(num)

#reverse order printing
simple_list.reverse()
print(simple_list)
