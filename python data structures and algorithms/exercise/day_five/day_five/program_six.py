"""
# @Name    :program_six.py
# @Author  :soundhar.B
# @Since   :15 Febuary 2021
# @Version :1.0
# @see     : program to print the pattern using while loop(#).



"""

#declaring the variables
start_one = 0
row = int(input("Enter the row : "))
column = int(input("Enter the column : "))
#looping
while  start_one < row :
    #variable declartion for inner loop
    start_two = 0
    while start_two<column: 
        print("#",end=" ")
        start_two+=1
    start_one+=1
    print("\n")

