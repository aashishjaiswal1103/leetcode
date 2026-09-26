# Last updated: 26/09/2026, 10:14:49
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, heada: ListNode, headb: ListNode) -> Optional[ListNode]:
9        a = heada
10        b = headb
11
12        while a != b:
13            a = a.next if a is not None else headb
14            b = b.next if b is not None else heada
15
16        return a