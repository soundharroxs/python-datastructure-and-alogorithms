"""
# @Name    : program_eight.py
# @Author  :soundhar.B
# @Since   : 15 Febuary 2021
# @Version :1.0
# @see     :  program to accept  5 tuple and find the length of element in tuple 
#             and store to dictionary.


"""
#declare the variable and empty list
length = 5
simple_list = [] 
#to get list of values and change to tuple
for lp in range(length):
    simple_string = input("Enter the string : ")
    simple_list.append(simple_string)
simple_tuple = tuple(simple_list)

#count and add to dictionary
simple_dict = {}
for lp_two in simple_tuple:
    count=0
    for lp_three in lp_two:
        count+=1
        simple_dict.update({lp_two:count})
        
#priting the dict
print("\nthe tuple ", simple_tuple)
print("\nthe dictionary ", simple_dict,"\n")