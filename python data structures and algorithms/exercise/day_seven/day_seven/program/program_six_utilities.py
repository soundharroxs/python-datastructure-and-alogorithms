
"""
	@python program
	@name : program_six_utilities.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and print number in words.

"""
"""
    Title : To Print number in words
    Args :
        Args1 : str_number is string input of number.
"""

class Word_number:
    @staticmethod
    def word_number(str_number):
        list_one = ["","one","two","three","four","five","six","seven","eight","nine"]
        list_two = ["","","twenty","thirty","fourty","fivty","sixty","seventy","eighty","ninety"] 
        list_three = ["ten","eleven","twelve","thirteen","fourteen","fiveteen","sixteeen","seventeen","eighteen","nineteen"]
        # if number is word then print zero else append to list
        if len(str_number) < 5:
            number = str_number.zfill(4)
            number_list = []
            if int(str_number) == 0:
                print("zero")
            else :
                for lp in number:
                    num = int(lp)
                    number_list.append(num) 
                # check the numberlist and print its  coresponding value to index value .
                if number_list[0] == 0:
                    pass
                else:
                    print(list_one[number_list[0]],"thousand ",end = " ")
                if number_list[1] == 0:
                    pass
                else:
                    print(list_one[number_list[1]],"hundred ",end = " ")
                if number_list[2] == 0 :
                    print(list_one[number_list[3]],"only",end = " ")
                elif number_list[2] == 1 :
                        print(list_three[number_list[3]],"only",end = " ")
                else:
                    print(list_two[number_list[2]], list_one[number_list[3]],"only",end = " ")

        else:
            print("Please ! Enter the number below 10000. ")

