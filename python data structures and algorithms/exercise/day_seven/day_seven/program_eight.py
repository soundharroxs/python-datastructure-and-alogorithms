import program.program_eight_utilities as operation
"""
	@python program
	@name : program_eight.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and to do operation .

"""
# getting a input from the user
string = input("Enter the string : ")
print("To do operation\nPress 1 for Reverse string\nPress 2 for change case\nPress 3 for length and divisor\nPress 4 for high character\nPress 5 or more for exit")
user_input = 0

# looping until the value user input is 5 or more.
while user_input <5:
    user_input = int(input("Enter the nunber for operation : "))
    operation.Alphabet.main(user_input,string)