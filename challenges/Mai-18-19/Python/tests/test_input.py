import context
import pytest
from context import solution

def test_serializer():
    Node = solution.Node
    node = Node('root', Node('left'), Node('right'))
    expected = " ".join(["root", "left", "-1", "-1", "right", "-1", "-1"])
    returned = solution.serialize(node)
    assert  returned == expected

def test_deserializer():
    Node = solution.Node
    serial = " ".join(["root", "left", "-1", "-1", "right", "-1", "-1"]) 
    node = Node('root', Node('left'), Node('right'))
    returned = solution.deserialize(serial)
    assert  returned.value == node.value
    assert  returned.left.value == node.left.value
    assert  returned.right.value == node.right.value

def test_input2():
    Node = solution.Node
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert solution.deserialize(solution.serialize(node)).left.left.value == 'left.left'
