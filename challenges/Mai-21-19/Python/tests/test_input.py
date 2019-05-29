import context
import pytest
from context import solution

def test_leftDepth():
    expected = 3
    Tree = solution.Tree
    the_tree = Tree(0,
                    left=Tree(0,
                         left=Tree(0,
                               left=Tree(0))),
                    right=Tree(0,
                               right=(Tree(0,
                                           left=Tree(0),right=Tree(0)))))
    result = the_tree._find_greatest_left_depth(the_tree)
    assert result==expected

def test_rightDepth():
    expected = 3
    Tree = solution.Tree
    the_tree = Tree(0,
                    left=Tree(0,
                         left=Tree(0,
                               left=Tree(0))),
                    right=Tree(0,
                          right=(Tree(0,
                                 right=Tree(0)))))
    result = the_tree._find_greatest_right_depth(the_tree)
    assert result==expected


def test_unival_subtrees():
    Tree = solution.Tree
    tree = Tree(0, 
                left=Tree(1), 
                right=Tree(0, 
                            left=Tree(1, Tree(1), Tree(1)),
                            right=Tree(0)))
    returned = solution.unival_subtrees(tree)
    assert returned == True


def test_input2():
    returned = False
    assert returned == False
