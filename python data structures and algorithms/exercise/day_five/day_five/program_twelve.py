"""
# @Name    : program_twelve.py
# @Author  :soundhar.B
# @Since   : 15 Febuary 2021
# @Version :1.0
# @see     : program to  accept the mark and print grade  using if else .



"""

# getting the input mark from the user 
mark = int(input("enter the mark : "))

# condition statement for grades to the mark
if mark >= 80:
    print("\nGrade A")
elif mark >= 70 and mark <= 79 :
    print ("\n Grade B")
elif mark >= 60 and mark <= 69 :
    print ("\n Grade C")
elif mark >= 50 and mark <= 59 :
    print ("\n Grade D")
elif mark <50 :
    print ("\n Grade E")