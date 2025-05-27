'''
Node {
	int data,
    Node* next
}
'''
'''
This function should return true/false if linked list is palindrome/not palindrome
'''
def isPalindrome(A):
  val=[]
  temp=A
  while temp is not None:
    val.append(temp.data)
    temp=temp.next
  reverse=[]
  for i in range(len(val)-1,-1,-1):
    reverse.append(val[i])
  if val==reverse:
    return True
  else:
    return False
  
