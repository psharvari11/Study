# Definition of Linked List Node

# class Node: 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.next = None

# Complete the function below

class Solution:
    def deleteDuplicates(self,head):
      curr=head.next
      temp=head
      if head==None or head.next==None:
        return head
      while curr!=None:
        while temp!=None and curr!=None and curr.data==temp.data:
          curr=curr.next
        temp.next=curr
        temp=curr
        if curr!=None:
          curr=curr.next
      return head
      
      
