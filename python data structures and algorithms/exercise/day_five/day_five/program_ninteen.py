"""
# @Name    : program_ninteen.py
# @Author  :soundhar.B
# @Since   : 19 Febuary 2021
# @Version :1.0
# @see     :  program to count a word in list and append to dictionary with key and values.

"""

#declaring the list and dictionary
sandwiches = ["ham", "chesse" , "roast beef", "ham", "chesse", "roast beef", "ham", "butter" ]
temp_list = []
new_dictionary = {}

#count and append to dictionary
for lp in sandwiches:
    if lp not in temp_list:
        temp_list.append(lp)

for lp_out in temp_list:
    count = 0
    for lp_in in sandwiches:
        if lp_out == lp_in :
            count+=1
    new_dictionary.update({lp_out:count})     

print("\n", new_dictionary)



  