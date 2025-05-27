'''
Node {
	int data,
    Node* node
}
'''
'''
This function should return head of final linked list. A and B are heads of two linked list
'''
def addTwoNumbers(A, B):
  temp=Node(None)
  curr=temp
  carry=0
  while A or B or carry>0:
    if A:
      va1=A.data 
    else:
      va1=0
    if B:
      va2=B.data 
    else:
      va2=0
    sum1=va1+va2+carry
    newNode=sum1%10
    carry= sum1//10
    curr.next=Node(newNode) 
    curr=curr.next
    if A:
      A=A.next
    if B :
      B=B.next
  return temp.next

##Approach 2: 
def addTwoNumbers(A, B):
  head1=A
  head2=B
  carry=0
  sum1=0
  temp=Node(0)
  curr=temp
  while head1!=None or head2!=None:
    sum1=carry
    if head1!=None:
      sum1+=head1.data
      head1=head1.next
    if head2!=None:
      sum1+=head2.data
      head2=head2.next
    if sum1>9:
      carry=1
    else:
      carry=0
    sum1=sum1%10
    curr.next=Node(sum1)
    curr=curr.next
  return temp.next

