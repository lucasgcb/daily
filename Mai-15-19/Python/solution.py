def possible_sums(the_list):
    """
    Get all possible sums in a list without repeating self.
    Return a list of all the sums.
    """
    sums = []
    for i in range(0, len(the_list)):
        for j in range(0, len(the_list)):
            if i == j:
                pass
            else:
                sums += [the_list[i] + the_list[j]]
    return sums


def adds_up(the_list, k):
    """
    Check if any of the sums add up to k.
    Return False if not.
    """
    sums = possible_sums(the_list)
    return any(sum == k for sum in sums)
