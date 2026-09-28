# Last updated: 28/09/2026, 11:41:09
1class Solution:
2    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
3        if not head or not head.next or k == 0:
4            return head
5
6        length = 0
7        prev = None
8        curr = head
9
10        while curr:
11            prev = curr
12            curr = curr.next
13            length += 1
14
15        tail = prev
16
17        k = k % length
18
19        if k == 0:
20            return head
21
22        count = 1
23        curr = head
24
25        while count < length - k:
26            curr = curr.next
27            count += 1
28
29        new_head = curr.next
30        curr.next = None
31        tail.next = head
32
33        return new_head