# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse second half of list
        second = slow.next
        prev = slow.next = None
        while second:
            second.next, prev, second = prev, second, second.next

        # Reorder list
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next