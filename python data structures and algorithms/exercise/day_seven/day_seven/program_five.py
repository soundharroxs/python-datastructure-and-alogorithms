import program.program_five_utilities as compare

"""
	@python program
	@name : program_five.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and compare tuples .

"""

# getting a user input tuple 1
tuple_one =()
print("Enter the tuple 1")
for number_one in range(1,5+1):
    user_input_one = int(input("enter the " + str(number_one) + " number : "))
    tuple_one+=(user_input_one,)

# getting a user input tuple 2
tuple_two =()
print("Enter the tuple 2")
for number_two in range(1,5+1):
    user_input_two = int(input("enter the " + str(number_two) + " number : "))
    tuple_two+=(user_input_two,)

#function call to utilities page
compare.not_matched(tuple_one,tuple_two)