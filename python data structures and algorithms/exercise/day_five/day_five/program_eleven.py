"""
# @Name    : program_eleven.py
# @Author  :soundhar.B
# @Since   : 17 Febuary 2021
# @Version :1.0
# @see     :  program to print patterns using for loop.


"""
#initalize the start and using if condition to eliminate the un wanted row.
start = 0 
end = 10
start_in = 0


start = 0 
end = 10
start_in = 0

while start < end :
    if end == 5:
        break
    end_in = end
    if end_in != 8: 
        while start_in < end_in:
            print(end, end  = " ")
            end_in = end_in - 1
    if end != 8:
        print(" ")
    end = end -1