# Delete Middle Node
# Definition of Linked List Node

# class Node: 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.next = None

# Complete the function below
def solve(head, N):
  if N==1:
    return None
  slow=head
  fast=head
  prev=None
  while(fast and fast.next):
    prev=slow
    slow=slow.next
    fast=fast.next.next
  prev.next=slow.next
  return head





# Description

# You are given the head of a linked list. Delete the middle node, and return
# the [JB] of the modified linked list.

# The middle node of a linked list of size n is the |n / 2Jth node from the
# start using 0-based indexing, where |x| denotes the largest integer less
# than or equal to x.

# Note: You don't have to take input or print output, just complete the
# function deleteMiddle() and return the head pointer of the modified list
# Input Description

# Input Format

# The first line contains the number of nodes, N

# The second line contains the values of nodes.

# Constraints

# 1<=N<=10"4