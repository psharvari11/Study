# Insert a node at the Tail
# Definition of Linked List Node

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Complete the function below

class Solution:
    def insertNodeAtTail(self,head,data):
      newnode=Node(data)
      if head is None:
        return newnode
      temp=head
      while temp.next != None:
        temp=temp.next
      temp.next=newnode
      return head
      
      






# Description

# You are given the pointer to the head node of a linked list and an integer
# to add to the list. Create a new node with the given integer. Insert this
# node at the tail of the linked list and return the head node of the linked list
# formed after inserting this new node. The given head pointer may be null,
# meaning that the initial list is empty.

# You have to complete the
# method. It takes two arguments: the head of the linked list
# and the integer to insert at the tail. You should not readany input from the
# stdin/console.

# Input Description

# The first line contains an integer n, denoting the elements of the linked
# list.

# The next nlines contain an integer each, denoting the element that needs
# to be inserted at the tail.

# Constraints

# 1<=n<=1000

# 1 <= list[i] <= 1000