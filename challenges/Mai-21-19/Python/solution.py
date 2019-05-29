class Tree:
    def __init__(self, value,right=None,left=None):
        self.value = value
        self.right = right
        self.left = left

    def print_tree(self):
        print("oi")

    def _find_greatest_left_depth(self,node,greatest=0):
        greatest_on_right = greatest
        greatest_on_left = greatest
        try:
            if node.left.value is not None:
                greatest_on_left += 1
                greatest_on_left = self._find_greatest_left_depth(node.left,greatest_on_left)
                
        except Exception:
            pass
        
        try:
            if node.right.value is not None:
                greatest_on_right -= 1
                greatest_on_right = self._find_greatest_left_depth(node.right,greatest_on_right)
        except Exception:
            pass
        
        return max([greatest_on_right,greatest_on_left])

    def _find_greatest_right_depth(self,node,greatest=0):
        greatest_on_right = greatest
        greatest_on_left = greatest
        try:
            if node.left.value is not None:
                greatest_on_left -= 1
                greatest_on_left = self._find_greatest_right_depth(node.left,greatest_on_left)
                
        except Exception:
            pass
        
        try:
            if node.right.value is not None:
                greatest_on_right += 1
                greatest_on_right = self._find_greatest_right_depth(node.right,greatest_on_right)
        except Exception:
            pass
        
        return max([greatest_on_right,greatest_on_left])

    def _print_root(self,root):
        pass

def unival_subtrees(bar):
    return False
