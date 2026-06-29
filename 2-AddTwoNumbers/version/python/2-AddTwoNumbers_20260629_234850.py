# Last updated: 29/06/2026, 23:48:50
# using carry
1class Solution:
2    def addTwoNumbers(self, l1, l2):
3        dummy = cur = ListNode()
4        carry = 0
5
6        while l1 or l2 or carry:
7            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
8
9            cur.next = ListNode(carry % 10)
10            cur = cur.next
11
12            carry //= 10
13
14            l1 = l1.next if l1 else None
15            l2 = l2.next if l2 else None
16
17        return dummy.next