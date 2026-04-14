# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        # Find middle of list
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse second half of list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        
        # Reorder list
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next

