# Last updated: 01/10/2026, 10:55:55
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
8        num1 = 0
9        num2 = 0
10        len1 = 0
11        len2 = 0
12
13        temp = l1
14        while temp:
15            len1 += 1
16            temp = temp.next
17
18        temp = l2
19        while temp:
20            len2 += 1
21            temp = temp.next
22
23        temp = l1
24        power = len1 - 1
25
26        while temp:
27            num1 += temp.val * (10 ** power)
28            power -= 1
29            temp = temp.next
30
31        temp = l2
32        power = len2 - 1
33
34        while temp:
35            num2 += temp.val * (10 ** power)
36            power -= 1
37            temp = temp.next
38
39        ans = num1 + num2
40
41        dummy = ListNode(-1)
42        curr = dummy
43
44        for digit in str(ans):
45            newnode = ListNode(int(digit))
46            curr.next = newnode
47            curr = newnode
48
49        return dummy.next