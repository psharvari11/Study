"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""
def maxDepth(root):
  if root is None:
    return 0
  else:
    left=maxDepth(root.left)
    right=maxDepth(root.right)
  return max(left,right)+1