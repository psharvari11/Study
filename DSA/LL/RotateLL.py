# Definition of Linked List Node

# class Node: 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.next = None

# Complete the function below

class Solution:
    def rotateRight(self,head,k):
      for k in range(k):
        i=head
        j=None
        while i.next!=None:
          j=i
          i=i.next
        j.next=None
        i.next=head
        head=i
      return head
      
