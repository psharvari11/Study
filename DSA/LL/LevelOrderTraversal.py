# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def levelOrder(self, root):
      res = []
      if not root:
        return []
      queue = [root]
      while queue:
        size = len(queue)
        nodes = []
        for i in range(size):
          node = queue.pop(0)
          nodes.append(node.val)
          if node.left :
            queue.append(node.left)
          if node.right :
            queue.append(node.right)
        res.append(nodes)
      return res     
