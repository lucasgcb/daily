class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
def deserialize(serialized_tree):
    # Split serialized tree into a list we can manipulate
    # Call the deserial class recursively starting with the head
    tree = serialized_tree.split(" ")
    head = Node(tree[0])
    tree_deserial(head,tree)
    return head

def tree_deserial(root_node,serialized_tree):
    # Pop an element from the serialized tree,
    # Verify it is not a null marker, apply value.
    # Initialize right and left,
    # then apply the same function over them
    # repeat this until the serial list is empty.
    null_marker = "-1"
    try:
        next_node = serialized_tree.pop(0)
    except IndexError:
        return

    if next_node == null_marker:
        root_node.value = None
        return
    else:
        root_node.value = next_node
        root_node.left = Node(None)
        root_node.right = Node(None)
        tree_deserial(root_node.left,serialized_tree)
        tree_deserial(root_node.right,serialized_tree)

def serialize(root_node:Node) -> str:
    # Put every node value in a list
    # return it as a string, separated with spaces.
    # Null nodes are represented by -1.
    serialized_tree = []
    tree_serial(root_node,serialized_tree)
    return " ".join(serialized_tree)
    
def tree_serial(root_node,serialized_tree) -> None:
    # Check if the node is null, mark -1 in the list and return if yes
    # Otherwise, put the node value in the list. 
    # Repeat this function with the node's left and right attributes.
    null_marker = "-1"
    if root_node == None:
        serialized_tree.append(null_marker)
        return
    else:
        serialized_tree.append(root_node.value)
        tree_serial(root_node.left, serialized_tree)
        tree_serial(root_node.right, serialized_tree)
