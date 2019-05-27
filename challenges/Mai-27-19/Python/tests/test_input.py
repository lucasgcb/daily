import context
import pytest
from context import solution



def test_potential_finder():
    """
    Find permutations that are potentially the desired solution,
    since the maximum solution size is given by the minimum step.
    """
    potentials = []
    possible_steps = [1,2]
    max_solution_size = len([1,2])
    expected = [(1,),(2,),(1,1),(1,2),(2,1),(2,2)]
    solution.potential_finder(max_solution_size, [], potentials, possible_steps)
    potentialsSet = set(tuple(row) for row in potentials)
    assert potentialsSet == set(expected)

def test_solver():
    """
    Find permutations that are potentially the desired solution,
    since the maximum solution size is given by the minimum step.
    """
    possible_steps = [1,3]
    expected = [(1,1,1),(3,)]
    max_solution_size = len([1,1,1])
    total_steps = 3
    result = solution.solver(max_solution_size,possible_steps,total_steps)
    
    assert set(result) == set(expected)

def test_first_solution():
    N = 4
    minimum_step = 1
    result = solution.first_solution(minimum_step, N)
    expected = (1,1,1,1)
    assert set(result) == set(expected)

def test_input():
    N = 4
    results = solution.climber_possibilities(N)
    expected = [ (1,1,1,1),
                 (2,1,1),
                 (1,2,1),
                 (1,1,2),
                 (2,2)]
    results = set(results)
    expected = set(expected)
    assert expected==results
    


def test_input2():
    returned = False
    assert returned == False
