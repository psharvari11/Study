# Definition of Linked List Node

# class Node: 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.next = None

# Complete the function below

class Solution:
    def hasCycle(self,head):
      if not head:
        return False
      i=head
      j=head
      while j and j.next:
        i=i.next 
        j=j.next.next
        if i==j:
          return True
      return False
  
