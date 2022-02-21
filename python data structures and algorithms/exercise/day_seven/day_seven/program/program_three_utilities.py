"""
	@python program
	@name : program_two.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form user and sort the list .

"""
"""
    Title : To sort number in ascending and descending.
    Args :
        Args1 : number_list gives number in list.
"""

class sort:
    def sorts(number_list):
        ascending_list = []
        # sorting the list
        while number_list:
            min_num  = number_list[0]
            for lp in number_list:
                if min_num > lp:
                    min_num =lp
            ascending_list.append(min_num)
            number_list.remove(min_num)
        dscending_list = ascending_list[::-1]
        print(" sorted array(Ascending)")
        # printing the number in order
        for lp_one in range(len(ascending_list)):
            print(lp_one+1,".",ascending_list[lp_one])
        print("\nsorted array(dscending)")
        for lp_two in range(len(dscending_list)):
            print(lp_two+1,".",dscending_list[lp_two])            
            