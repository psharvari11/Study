'''
Node {
	int data,
    Node* node
}
'''
'''
This function should return head of merged linked list
'''
#Return head of reversed linked list
def reverse(A):
  res=None
  prev=None
  curr=A
  while curr!=None:
    res=curr.next
    curr.next=prev
    prev=curr
    curr=res
  return prev
  
  
