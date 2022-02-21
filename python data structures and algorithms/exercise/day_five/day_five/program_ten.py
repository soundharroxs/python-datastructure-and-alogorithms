"""
# @Name    : program_ten.py
# @Author  :soundhar.B
# @Since   : 16 Febuary 2021
# @Version :1.0
# @see     :  program to print patterns using for loop.


"""
# printing the number by inverted triangle using for and if condition
for out_lp in range(10,0,-1):
    if out_lp == 9 or out_lp == 4 or out_lp == 5 :
        continue
    for in_lp in range(out_lp):
        print(out_lp,end=" ")
    print(" ")