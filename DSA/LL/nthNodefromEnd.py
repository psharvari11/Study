'''
Node {
	int data,
    Node* next
}
'''
'''
This function should return value of nth node from the end.
'''
def nthNode(A, n):
  slow=A
  fast=A
  while n>0:
    fast=fast.next
    n-=1
  while fast!=None:
    fast=fast.next
    slow=slow.next
  return slow.data
  
