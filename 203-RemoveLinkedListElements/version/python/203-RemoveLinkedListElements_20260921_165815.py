# Last updated: 21/09/2026, 16:58:15
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
8        while head is not None and head.val == val:
9            head = head.next
10
11        current = head
12
13        while current is not None and current.next is not None:
14            if current.next.val == val:
15                current.next = current.next.next
16            else:
17                current = current.next
18
19        return head   