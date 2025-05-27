# Deleting a Node
# Definition of Linked List Node

# class Node: 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.next = None

# Complete the function below

class Solution:
    def deleteNode(self,head,position):
      if head is None:
        return None
      if position == 0:
        return head.next
      curr = head
      count = 0
      while curr and count<position-1:
        curr=curr.next
        count+=1
      if not curr:
        return head
      curr.next=curr.next.next
      return head      




# Description

# Delete the node at a given position in a linked list and return a reference
# to the head node. The head is at position 0. The list may be empty after
# you delete the node. In that case, return a null value.

# Complete thedeleteNodefunction in the editor below.

# deleteNodehas the following parameters:

# -LinkedListNode pointer list:a reference to the head node in the list

# -int position:the position of the node to remove

# Input Description

# The first line of input contains an integer n, the number of elements in the
# linked list.

# Each of the next n lines containsan integer, the node data values in order.
# The last line contains an integer the position of the node to delete.
# Constraints

# 1<=n<=1000

# 1 <= list{i] <= 1000