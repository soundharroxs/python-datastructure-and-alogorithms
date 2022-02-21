"""
	@python program
	@name : program_eight_utilities.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and to do operation .

"""
"""
    Title :  To do operation Reverse string, change case ,length and divisor, high character.
    Args :
        Args1 : string - input a string from user.
        Args2 : input_selection is number .
"""
class Alphabet:
    @classmethod
    def main(cls,input_selection,string):
        if input_selection == 1:
            cls.reverse_string(string)
        elif input_selection == 2:
            cls.case_types(string)
        elif input_selection == 3:
            cls.lenth_divsor(string)
        elif input_selection == 4 :
            cls.high_charater(string)
        else:
            print("Exit the program")

    @staticmethod
    def reverse_string (string):
        reverse = ""
        for lp in string:
            reverse = lp +reverse
        print("The reverse of string : ", reverse)


    @staticmethod  
    def case_types(string):
        init_cap= string.capitalize()
        lower = string.lower()
        upper = string.upper()
        print("the inital capitalize :", init_cap)
        print("The lower case : ", lower)
        print("The upper case :", upper)

    @staticmethod
    def lenth_divsor(string):
        length = len(string)
        print("The length of string is : ",length)
        for lp in range(1,length):
            if length % lp == 0:
                print("The divisor of string : ",lp,end = " ")

    @staticmethod
    def high_charater(string):
        maximun = string[0]
        for lp_in in string:
            if ord(lp_in) > ord(maximun):
                maximun = lp_in
        print("The highest character is : ", maximun)


