class Tree:
    def __init__(self, value,right=None,left=None):
        self.value = value
        self.right = right
        self.left = left

    def find_univals(self,root):
        """
        Return the size of the unival list.
        """
        univals_list = []
        self._unival_finder(root,univals_list)
        return len(univals_list)

    def _unival_finder(self, node, univals_list):    
        """
        Recursively check the tree, and add an unival to the list if:
        both the current, right and left nodes hold the same value,
        or both right and left nodes of the current node are None
        """
        
        right_is_equal = False
        right_is_None = False
        left_is_None = False
        left_is_equal = False

        try:
            left_is_equal = (node.left.value == node.value)
            self._unival_finder(node.left,univals_list)
        except Exception:
            left_is_None = True 

        try:
            right_is_equal = (node.right.value == node.value)
            self._unival_finder(node.right,univals_list)
        except Exception:
            right_is_None = True
        
        if right_is_equal and left_is_equal or left_is_None and right_is_None:
            univals_list.append(node)
        
    def _print_root(self,root):
        pass

def unival_subtrees(bar):
    return False
