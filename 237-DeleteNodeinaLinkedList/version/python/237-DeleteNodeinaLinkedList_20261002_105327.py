# Last updated: 02/10/2026, 10:53:27
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def deleteNode(self, node):
9        """
10        :type node: ListNode
11        :rtype: void Do not return anything, modify node in-place instead.
12        """
13        curr = node
14        while curr.next:
15            curr.val = curr.next.val
16            if curr.next.next is None:
17                curr.next = None
18                break
19            curr = curr.next
20
21        
22        