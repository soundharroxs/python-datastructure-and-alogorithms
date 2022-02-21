"""
# @Name    : program_five.py
# @Author  :soundhar.B
# @Since   : 15 Febuary 2021
# @Version :1.0
# @see     :  program to fibonacci series.

"""
#decalring the variables
num_one = 0
num_two = 1
limit = 20 

print("\nFibonacci series")
#loop for number of times the fibonacci series should print
for i in range(limit):
    print(num_one)
    #finding avg
    avg = num_one/limit
    #swaping the variables for add and move to the next number
    temp = num_one + num_two
    num_one = num_two
    num_two = temp

print("\nThe average of fibonacci series is {} ".format(avg))
