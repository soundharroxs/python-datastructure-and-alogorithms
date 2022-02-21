import program.program_three_utilities as mod
"""
	@python program
	@name : program_two.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form user and sort the list .

"""


# get list  input from the user
simple_list = []
for lp  in range(1,11):
    user_input = int(input("Enter  "+str(lp)+ "number in the list : "))
    simple_list.append(user_input)


# function call to the utilities.
mod.sort.sorts(simple_list)