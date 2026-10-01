# Last updated: 01/10/2026, 11:43:44
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNodes(self, head: ListNode | None) -> ListNode | None:
8        stack =[]
9        curr= head
10        while curr!=None :
11            while stack and curr.val > stack[-1].val:
12                stack.pop()
13
14            stack.append(curr)
15            curr=curr.next
16        dummy =ListNode(-1)
17        current = dummy
18        for node in stack:
19            current.next = node
20            current=node
21        return dummy.next
22
23