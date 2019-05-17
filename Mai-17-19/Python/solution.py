import copy
from functools import reduce


def new_array(the_list : list) -> list:
    """
    Return a new array where each index is a product
    of all the other elements except for itself. 
    """
    new_list = [0] * len(the_list) # Init a list of
                                   # the same size. 
    for i in range(0,len(the_list)):
        new_list[i] = reduce(lambda a,b:a*b,the_list)
        # Reduce feeds 'a' back into the anon function, 
        # unpacking each multiplier into 'b'.
        new_list[i] /= the_list[i]
        # Remove the effect of repeated index.
    return new_list


def return_all_except(index,the_list):
    """
    Return a list with every multiplier, minus index,
    preserving original list.
    """
    temp = copy.deepcopy(the_list) # create a copy of the list
    temp.pop(index) # pop the desired index from the list
    return temp # return

def new_array_no_division(the_list : list) -> list:
    """
    Return a new array where each index is a product
    of all the other elements except for itself. 
    """
    new_list = [0] * len(the_list) # Init a list of
                                   # the same size. 
    for i in range(0,len(the_list)):
        multipliers = return_all_except(i,the_list)
        new_list[i] = reduce(lambda a,b: a*b, multipliers)
        # Reduce feeds 'a' back into the anon function, 
        # unpacking each multiplier into 'b'.
    return new_list


