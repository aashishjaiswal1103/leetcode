# Last updated: 29/09/2026, 10:47:17
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7
8    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
9
10        if head is None or head.next is None:
11            return head
12
13        curr = head
14        nxt = head.next
15
16        while nxt:
17            if curr.val == nxt.val:
18                nxt = nxt.next
19            else:
20                curr.next = nxt
21                curr = nxt
22                nxt = nxt.next
23        curr.next = None 
24        return head