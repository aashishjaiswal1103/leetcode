# Last updated: 01/10/2026, 10:42:42
1class Solution:
2    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
3        dummy = ListNode(-1)
4        curr = dummy
5        carry = 0
6
7        while l1 or l2:
8            ans = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
9
10            value = ans % 10
11            carry = ans // 10
12
13            newnode = ListNode(value)
14            curr.next = newnode
15            curr = newnode
16
17            if l1:
18                l1 = l1.next
19
20            if l2:
21                l2 = l2.next
22
23        if carry:
24            newnode = ListNode(carry)
25            curr.next = newnode
26
27        return dummy.next