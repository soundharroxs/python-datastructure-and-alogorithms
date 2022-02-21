"""
	@python program
	@name : program_one_utilities.py
	@date : 3/4/2021
	@author: soundhar.B
	@since : python program to calculate the compound intrest .

"""


"""
    Title : To find the compound interest.
    Args :
        Args1 : principle will get the amount entered by the user.
"""

class Compound_interest:

    @staticmethod
    def compound_interest(principle):
        rate = [ 12 , 11.6, 16.2 ,17.1]
        time = [0.5, 1, 2, 3, 4, 5]
        year = ["6 month", "1 year ", "2 year", "3year", "4 year", "5 year"]
        print("Interest rate for 5 years")
        print("Amount","\t","year","\t","12%","\t" "11.6%", "\t","16.2%","\t" "17.1%")
        # to find the intrest amount.
        for lp_out in time:
            print (principle,"\t",lp_out,"\t",end = "")
            for lp_in in rate:
                amount = principle * (pow((1 + lp_in / 100),lp_out))
                #round of the amount
                print(round(amount,0),end = " ")
            print("")

