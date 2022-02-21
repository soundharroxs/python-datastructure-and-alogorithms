"""
# @Name    : program_sixteen.py
# @Author  :soundhar.B
# @Since   : 16 Febuary 2021
# @Version :1.0
# @see     :  program to compare two list and update a new list if list value does not match.

"""

#delcare lists
list_one = [1,2,3,4,5,22,54,67,21,33]
list_two = [1,2,4,4,8,66,32,22,12,21]
list_three = []

# append the items in empty if not present in list two
for i in list_one:
    if i not in list_two :
        list_three.append(i)
## append the items in empty if not present in list one
for j in list_two:
    if j  not in list_one:
        list_three.append(j)
    
#printing the new list with while loop  
length = len(list_three)
start = 0
# Iterating using while loop
while start < length:
    print(list_three[start],end = " ")
    start += 1


