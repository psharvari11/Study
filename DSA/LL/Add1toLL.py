'''
Node {
	int data,
    Node* node
}
'''
'''
This function should return head of merged linked list
'''
#Return head of new linked list
def addOne(A):
  A=reverse(A)
  i=A
  j=0
  carry=1
  while i:
    sum1=i.data+carry
    carry=sum1//10
    i.data=sum1%10
    j=i
    i=i.next
  if carry>0:
    j.next=Node(carry)
  return reverse(A)
def reverse(A):
  i=A
  j=None
  while i:
    new=i.next
    i.next=j
    j=i
    i=new
  return j
  
