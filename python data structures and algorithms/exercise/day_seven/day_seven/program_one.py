import program.program_one_utilities as function

"""
	@python program
	@name : program_one.py
	@date : 4/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and print the compound interest .

"""

# get a user input.
input_amount = int(input("Enter the amount : "))

#function call to program one utilities file
function.Compound_interest.compound_interest(input_amount)