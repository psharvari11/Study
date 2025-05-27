
# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.next = None

# return head of new linked list

def fillGaps(head):
  curr=head
  while curr!=None and curr.next!=None:
    temp=curr.next
    dif=temp.data-curr.data
    if dif>1:
      new=Node(curr.data+1)
      curr.next=new
      new.next=temp
    curr=curr.next  
  return head

