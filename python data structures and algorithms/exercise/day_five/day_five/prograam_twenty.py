"""
# @Name    : program_twenty.py
# @Author  :soundhar.B
# @Since   : 19 Febuary 2021
# @Version :1.0
# @see     : program to print divisor of the number and print even divisor.



"""
#declare and get the input number
input_number = int(input("Enter the number : "))
divisor = []

# loop and eliminate the odd divisor
for lp in range(1,input_number+1):
    if input_number % lp == 0 and lp % 2 == 0:
        divisor.append(lp)

print("\n The divisor of {} are : " .format(input_number) , divisor)