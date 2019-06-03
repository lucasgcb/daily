def find_longest(s,k):
    substrings = []
    # Generate all inputs for GO to process.
    # variations of the original input with the first value popped,
    # this was just the less messy way as opposed to 
    # iterating with pop and the actual list input.
    # Could be easily optimized, but debugging like this is way better.
    inputs = [s[i:] for i in range(0,len(s))]
    for input_sequence in inputs:
        GO(k,input_sequence,substrings)

    # Return the value in the list with the greatest len() result.
    return max(substrings,key=len)

def GO(k,input_sequence,substrings_list):
    # Procedurally go through input sequence and 
    # append the character to the substring. 
    # If the next character is not in the substring, reduce k by 1. 
    # Once the sequence is over, or k is below 0,
    # end the sequence.
    substring = ""
    for next_character in input_sequence:
        if next_character not in substring:
            k-=1
        if k<0:
            return end(substrings_list,substring)
        substring += next_character
    return end(substrings_list,substring)

def end(substrings_list,substring):
    # Append the substring into the substrings list.
    # This works by reference so returning here doesn't actually do anything.
    substrings_list.append(substring)
    return substrings_list


