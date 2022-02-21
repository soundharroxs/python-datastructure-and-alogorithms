"""
	@python program
	@name : program_seven.py
	@date : 04/3/2021
	@author: soundhar.B
	@since : python program for get input form the user and sort a string . .

"""
"""
    Title : sort a string
    Args :
        Args1 : string pass a string input.
"""
def sort_string(string):
    string_list = []
    sort_list = []
    # remove the white spaces.
    modified_string = string.replace(" ","")
    # change to lower case
    lower_string = modified_string.lower()
    for lp in lower_string:
        string_list.append(lp)
    while string_list:
        minimun = string_list[0]
        for lp_in in string_list:
            # check the ascii value and sorts.
            if ord(lp_in) > ord(minimun):
                minimun = lp_in
        sort_list.append(minimun)
        string_list.remove(minimun)
    simple_string = ""
    print("Given String : ",string)
    print("Ascending order : ", simple_string.join(sort_list))
    print("Descending order : ", simple_string.join(sort_list[::-1]))     
