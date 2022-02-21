"""
# @Name    : program_one.py
# @Author  :soundhar.B
# @Since   : 12 Febuary 2021
# @Version :1.0
# @see     :  program to accept month and date using if and list.


"""
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key ,':', p_info[key])