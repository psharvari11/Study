# Insert a node at the Head



'''
class Node {
	int data,
    Node* next
}
'''
'''
This function should return new head of linkedlist.
'''
def insertNodeAtHead(head, data):
	newnode=Node(data)
	newnode.next=head
	head=newnode
	return head




# Description

# Given a pointer to the head of a linked list, insert a new node before the
# head. Return a reference to the new head of the list. The head pointer
# given may be null meaning that the initial list is empty.

# Complete the function insertNodeAtHead in the editor below.
# insertNodeAtHeadhas the following parameter(s):

# LinkedListNode list: a reference to the head of a list

# data: the value to insert in the data field of the new node

# Input Description

# The first line contains an integer n, the number of elements to be inserted
# at the head of the list.

# The next n lines contain an integer each, the elements to be inserted, one
# per function call.