"""
# @Name    : program_thirteen.py
# @Author  :soundhar.B
# @Since   : 17 Febuary 2021
# @Version :1.0
# @see     :  program to color code and color name using dictionary



"""
# create a dictinory 
color_dict = {
    1:"red",  2:"blue",  3:"green",  4:"yellow",  5:"orange",
    6:"black",  7:"white",  8:"brown",  9:"pink",  10:"grey"
}

# getting the user value
color_code = int(input("\n Color code : "))

print("\n Color name :", color_dict.get(color_code,"color name does not exit"))