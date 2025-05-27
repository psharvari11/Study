'''
Node {
	int data,
    Node* node
}
'''
'''
This function should return head of merged linked list
'''
def mergeLists(A, B):
  head1=A
  head2=B
  res=Node(-1)
  i=res
  while head1!=None and head2!=None:
    if head1.data<=head2.data:
      i.next=head1
      head1=head1.next
    else:
      i.next=head2
      head2=head2.next
    i=i.next
  if head1!=None:
    i.next=head1
  if head2!=None:
    i.next=head2
  return res.next
  
  
