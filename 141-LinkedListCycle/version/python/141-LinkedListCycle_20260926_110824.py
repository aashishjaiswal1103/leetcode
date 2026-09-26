# Last updated: 26/09/2026, 11:08:24
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow = head 
10        fast = head 
11        while fast is not None and fast.next is not None :
12            slow = slow.next
13            fast = fast.next.next
14            if fast is not None and slow==fast :
15                return True 
16        return False 