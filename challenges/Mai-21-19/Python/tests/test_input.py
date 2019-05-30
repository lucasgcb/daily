import context
import pytest
from context import solution

def test_unival_subtrees():
    Tree = solution.Tree
    tree = Tree(0, 
                left=Tree(1), 
                right=Tree(0, 
                            left=Tree(1, Tree(1), Tree(1)),
                            right=Tree(0)))
    returned = tree.find_univals(tree)
    assert returned == 5

