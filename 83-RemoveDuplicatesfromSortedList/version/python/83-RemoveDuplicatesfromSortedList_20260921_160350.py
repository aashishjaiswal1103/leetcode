# Last updated: 21/09/2026, 16:03:50
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
8        if head is None:
9            return None
10
11        first = head
12        second = first.next
13
14        while second is not None:
15            if first.val == second.val:
16                first.next = second.next
17                second = second.next
18            else:
19                first.next = second
20                first = second
21                second = second.next
22
23        return head   