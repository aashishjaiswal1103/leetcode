# Last updated: 21/09/2026, 16:57:52
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
8        current = head
9        count = 0
10
11        # Find length
12        while current:
13            count += 1
14            current = current.next
15
16        k = count - n
17
18        if k == 0:
19            return head.next
20
21        current = head
22        countk = 0
23
24        while countk < k - 1:
25            current = current.next
26            countk += 1
27
28        current.next = current.next.next
29
30        return head
31        