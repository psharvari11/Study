# Insert at a specific position

# Definition of Linked List Node

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Complete the function below

class Solution:
    def insertNodeAtaPosition(self,head,data,position):
      value=1
      temp=head
      while value!=position and temp!=None:
        temp=temp.next
        value+=1
      newNode=Node(data)
      if position==0:
        newNode.next=head
        head=newNode
      else:
        ans=temp.next
        temp.next=newNode
        newNode.next=ans
      return head
      




# Description

# Given the pointer to the head node of a linked list and an integer to insert
# at a certain position, create a new node with the given integer as its data
# attribute, insert this node at the desired position and return the head
# node.

# A position of 0 indicates head, a position of 1 indicates one node away
# from the head, and so on. The head pointer given may be null meaning
# that the initial list is empty.

# Complete the functioninsertNodeAtPositionin the editor below. It must
# return a reference to the head node of your finished list.
# insertNodeAtPosition has the following parameters:

# head: a SinglyLinkedListNode pointer to the head of the list

# data: an integer value to insert as data in your new node

# position: an integer position to insert the new node, zero-based indexing