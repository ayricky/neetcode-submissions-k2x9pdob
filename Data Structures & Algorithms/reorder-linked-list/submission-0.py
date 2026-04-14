# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            second.next, prev, second = prev, second, second.next
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



#     [0, 1, 2, 3, 4, 5, 6]        
#           slow^    
#                    fast^
# 

        