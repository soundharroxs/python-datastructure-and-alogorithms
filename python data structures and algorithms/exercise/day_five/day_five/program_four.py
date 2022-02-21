"""
# @Name    : program_one.py
# @Author  :soundhar.B
# @Since   : 12 Febuary 2021
# @Version :1.0
# @see     :  program to find sum of number and average of it using do while loop.




"""

start_num = 1
end_num = 100
add = 0
while True:
    add = add + start_num
    start_num = start_num + 1
    if(start_num > end_num):
        break

avg = add/end_num
print("\n the sum of number {} to {} is {}" .format(start_num,end_num,add))
print("\n the average of number {} to {} is {}" .format(start_num,end_num,avg))