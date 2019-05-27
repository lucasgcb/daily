def cons(a, b):
    ## Construct a higher order function that returns an input pair
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    # f will fold the values into the function that gets input.
    # Return a function that takes two inputs and returns the first result.
    return f(lambda a,b: a)

def cdr(f):
    # f will fold the values into the function that gets input.
    # Return a function that takes two inputs and returns the first result.
    return f(lambda a,b: b)


### More readable solutions

def car_alt(f):
    def return_first_input(a,b):
        return a
    # f will fold the values into the function that gets input.
    # Return a function that takes two inputs and returns the first result.
    return f(return_first_input)

def cdr_alt(f):
    def return_second_input(a,b):
        return b
    # f will fold the values into the function that gets input.
    # Return a function that takes two inputs and returns the first result.
    return f(return_second_input)