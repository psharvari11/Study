"""
Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reversepair(self, head: ListNode) -> ListNode:
      if head is None or head.next is None:
        return head
      temp=head.next
      ans=self.reversepair(head.next.next)
      head.next=ans
      temp.next=head
      return temp