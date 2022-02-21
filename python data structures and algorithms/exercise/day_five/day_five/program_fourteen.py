"""
# @Name    : program_fourteen.py
# @Author  :soundhar.B
# @Since   : 18 Febuary 2021
# @Version :1.0
# @see     :  program to print states and capital in dictonary as given.

"""
#declaring the dictionary
states_and_capitals = {
    "Gujarat":"Gandhinagar", "Maharashtra":"Mumbai", "Rajasthan":"Jaipur", "Bihar":"Patna",
    "Tamil Nadu":"Chennai","Kerala":"Thiruvananthapuram", "Nagaland":"Kohima", "Punjab":"Chandigarh",
    "Uttar Pradesh":"Lucknow", "West Bengal":"Kolkata","Assam":"Dispur", "Andhra":"Hyderabad", "Goa":"panaji"
}
#getting the user value
statename = input("Enter the state the name : ")
#dictionary as switch to find the key and value .
for lp in states_and_capitals:
    if statename.lower() == lp.lower():
        print("Capital of {} is {}".format(statename,states_and_capitals.get(lp)))
        break
  
else:
    (print("\n The states in dictionary : " ,states_and_capitals.keys()))
