# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Obervalo como: pointer -> [val:0|dummy|next] -> [val|list1|next] -> ... no como un array
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        pointer = dummy

        #Verifica que la lista no este vacía.
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next

        if list1:
            pointer.next = list1
        else:
            pointer.next = list2
        return dummy.next 

            



