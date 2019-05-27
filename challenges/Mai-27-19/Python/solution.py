
def first_solution(minimum_step,total_steps):
    """
    Find the first, longest combination utilizing the minimum_step.
    """

    solution = []
    for _ in range(0,total_steps):
        solution.append(minimum_step)
    return tuple(solution)

def potential_finder(max_solution_size, potential, potentials, possible_steps):
    """
    Find permutations that are potentially the desired solution,
    since the maximum solution size is given by the minimum step.
    """
    from copy import deepcopy
    if not(len(potential) > max_solution_size):
        if len(potential) > 0:
            potentials.append(potential)
        for step in possible_steps:
            next_potential = deepcopy(potential)
            next_potential.append(step)
            potential_finder(max_solution_size,next_potential,potentials,possible_steps)
    return

def solver(max_solution_size, possible_steps, total_steps):
    """
    Filter through solutions found in potential candidates (combinations that == number of steps).
    """
    potentials = []
    ack =[]
    potential_finder(max_solution_size, ack, potentials, possible_steps)
    potentials = filter(lambda potential_solution:sum(potential_solution)==total_steps, potentials)
    return set(tuple(row) for row in potentials)

def climber_possibilities(total_steps):
    """
    Figure out the longest solution, generate permutations based on the longest solution,
    then filter out the permutations that correspond to paths. Return the paths as tuples.
    """
    possible_steps = [1,2]
    start_solution = first_solution(possible_steps[0],total_steps)
    max_solution_size = len(start_solution)
    head = solver(max_solution_size, possible_steps, total_steps)
    return set(tuple(row) for row in head)