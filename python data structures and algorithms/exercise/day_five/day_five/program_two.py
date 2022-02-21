"""
# @Name    :program_two.py
# @Author  :soundhar.B
# @Since   :15 Febuary 2021
# @Version :1.0
# @see     :program to accpet mark and print pass and fail .


"""
# decalring the tuple
mark_tuple = ("35", "54", "65", "75", "33", "42", "29")

# loop the tuple and ,
# if mark is more than 50 it print if statement and flase print else statement
for element in mark_tuple:
    mark = int(element)
    if mark >= 50 :
        print("\nmark {} is pass".format(mark))

    else :
        print("\nmark {} is fail".format(mark))