
"""
	@python program
	@name : program_four_utilities.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program to print amstrong , perfect and prime_number. .

"""
"""
    Title : to find perfect number
    Args :
        Args1 : no args range is 1 to 1000
"""

def perfect_number():
    print("\nperfect number :",end = " ")
    for lp in range(1,1001):
        add = 0
        for lp_in in range(1,lp):
            if lp % lp_in == 0:
                add += lp_in
        if add == lp :
            print(lp,end=" ")


"""
    Title : to find Amstrong number
    Args :
        Args1 : no args range is 1 to 1000
"""

def amstrong_number():
    print("amstrong_number :",end=" ")
    for number in range(1, 1001):
        add = 0
        length = len(str(number))
        temp = number
        while temp:
            digt = temp % 10
            power = pow(digt,length)
            add += power
            temp = temp // 10

        if number == add:
            print (number,end = " ")

"""
    Title : to find Prime number
    Args :
        Args1 : no args range is 1 to 1000
"""

def prime_number():
    print("\nprime number :",end=" ")
    for num in range(1, 1000 + 1):
        if num > 1:
            for lp in range(2, num):
                if (num % lp) == 0:
                    break
            else:
                print(num, end =" ")