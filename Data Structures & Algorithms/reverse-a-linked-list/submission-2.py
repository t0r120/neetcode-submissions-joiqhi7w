# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Exit condition
        if not head:
            return None
        
        new_head = head # New head is the head by default
            #new_head will store the current in reverseList Box
        if head.next != None:
#-> If there is a node after the current node then...
            new_head = self.reverseList(head.next)
#-> new_head will have the next reverseList box newHead value
            head.next.next = head
        head.next = None
        return new_head




       
            
        
        

        

            
        