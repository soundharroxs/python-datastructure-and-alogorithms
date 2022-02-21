
"""
	@python program
	@name : program_two_utilities.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program to print tables .

"""

"""
    Title : To Print tables in given pattern
    Args :  No Args
"""

class Timetable:
    @staticmethod
    def time_table():
        print("*","\t","|","\t","10","\t","11","\t","12","\t","13","\t","14","\t","15","\t","16","\t","17","\t","18","\t","19","\t","20")    
        print("----------------------------------------------------------------------------------------------------")
        # tables from 1 to 15
        for lp_out in range(1,16):
            print(lp_out,"\t","|",end = "\t")
            # In the range of 10 to 20
            for lp_in in range (10,21):
                print(lp_out*lp_in, end = "\t")
            print("")


