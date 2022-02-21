def binary_search(list_,x):
    low_bound = 0
    upper_bound = len(list_)-1
    while low_bound <= upper_bound:
        mid_point = (low_bound + upper_bound)//2
        if list_[mid_point] == x:
            print("found",list_[mid_point])
            break
        else:

            if list_[mid_point] < x:
                low_bound = mid_point
            else:
                upper_bound = mid_point


list1 = [1,2,3,42,23,344,4242,66666]
x= 344
binary_search(list1,x)

















list_ = [1, 3, 14, 2, 5, 67, 8, 96, 2]
x = 1
binary_search(list_, x)













