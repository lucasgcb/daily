def number_finder(number_list):
    """
    This finds the missing integer using 2O(n) if you count the set operation.
    """
    numbers = list(set(number_list)) ## Order the list
    # Performance of set is O(n)
    # https://www.oreilly.com/library/view/high-performance-python/9781449361747/ch04.html
    expected_in_seq = None
    # We go through the list again. 2*O(n)
    for i in range(0,len(numbers)):
        expected_in_seq =  numbers[i] + 1
        ## Check if we are at the end of the list.
        try:
            next_in_seq = numbers[i+1]
        except IndexError:
            # Return the next positive expected in sequence if we are.
            return 0 if numbers[i] < 0 else expected_in_seq
        
        if expected_in_seq != next_in_seq:
            return expected_in_seq
            
