"""
	@python program
	@name : program_five_utilites.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and compare tuples .

"""

"""
    Title : compare tuples.
    Args :
        Args1 : tuple_one - tuple of 10 numbers
        Args2 : tuple_two - tuple of 10 numbers
"""

def not_matched(tuple_one,tuple_two):
    num_list = []
    # compare and append to new list
    for lp_one in tuple_one:
        if lp_one not in tuple_two:
            num_list.append(lp_one)
    for lp_two in tuple_two:
        if lp_two not in tuple_one:
            num_list.append(lp_two)
    print("Noy matched data :",tuple(num_list))
    
