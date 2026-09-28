# Last updated: 28/09/2026, 11:10:36
1class Solution:
2    def swapPairs(self, head: ListNode | None) -> ListNode | None:
3        if not head or not head.next:
4            return head
5
6        dummy = ListNode(0)
7        dummy.next = head
8
9        prev = dummy
10        curr = head
11        nxt = curr.next
12
13        while nxt is not None:
14            curr.next = nxt.next
15            nxt.next = curr
16            prev.next = nxt
17
18            prev = curr
19            curr = curr.next
20
21            if curr is None:
22                break
23
24            nxt = curr.next
25
26        return dummy.next