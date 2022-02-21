"""
# @Name    : program_nine.py
# @Author  :soundhar.B
# @Since   : 16 Febuary 2021
# @Version :1.0
# @see     : program to accept a combination of 10 number in the list

"""
#declaring the variables
list_ = []
even_list = []
ood_list = []
input_list_length = int(input("Enter the length of the list : "))

#geting the elements in list using for loop
for lp in range(0,input_list_length):
	elements = int(input("Enter the list element : "))
	list_.append(elements)

 #finding even and in the list    
for number in list_:
    if number % 2 == 0 :
        even_list.append(number)
        
    else:
        ood_list.append(number)

# printing the list elements with answers
print("\n  The list : ", list_)
print("\n 1. Maximum of list :", max(list_))
print("\n 2. Sum of list : ", sum(list_))

print("\n 3.Odd elements in list  :", ood_list)
print("   Even elements in list : ", even_list)

list_.reverse()
reverse_list = list_
print("\n 4. Rverse order of the list : ", reverse_list)