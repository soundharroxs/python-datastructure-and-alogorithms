"""
# @Name    : program_fivteen.py
# @Author  :soundhar.B
# @Since   : 18 Febuary 2021
# @Version :1.0
# @see     : program to related to states and dictionary.

"""
#create the dictionay and empty list
states_and_capitals = {
     "Gujarat":"Gandhinagar",
     "Maharashtra":"Mumbai",
     "Rajasthan":"Jaipur",
     "Bihar":"Patna",
     "Tamil Nadu":"Chennai",
     "Kerala":"Thiruvananthapuram",
     "Nagaland":"Kohima",
      "Punjab":"Chandigarh",
      "Uttar Pradesh":"Lucknow",
      "West Bengal":"Kolkata",
      "Assam":"Dispur",
     "Andhra":"Hyderabad",
      "Goa":"panaji"
}

states = []
capitals =[]
#append state to list and capital to tuple 
for state,capital in states_and_capitals.items() :
    states.append(state)
    capitals.append(capital)

capitals_tuple = tuple(capitals)
print("\n The list of states is : ", states)
print("\n The capital of tuple is : ", capitals_tuple)

new_dict = {}
# update  capital to key and value to state in new dictionary .
for lp in range(len(capitals)):
    new_dict.update({capitals_tuple[lp]:states[lp]})

print("\n The new dictionary is : ", new_dict)