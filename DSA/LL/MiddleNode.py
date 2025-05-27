# Middle Node
# Definition of Linked List Node

# class Node: 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.next = None

# Complete the function below

class Solution:
    def middleNode(self,head):
      slow=head
      fast=head
      while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
      return slow.data
      





# Description

# Given a non-empty, singly linked list with the head node [TER] .
# return a middle node of the linked list.

# If there are two middle nodes, return the second middle node.
# Complete the function$\spacesbelow, no need to take any input.
# Input Description

# The first line contains the number of nodes (t)

# Next t lines contains the node of the linked list
# Constraints

# 1 <=t<=1000

# 1 <= list[i] <= 1000

# Output Description

# Complete the function