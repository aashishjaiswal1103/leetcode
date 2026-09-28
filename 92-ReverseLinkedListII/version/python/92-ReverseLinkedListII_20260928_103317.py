# Last updated: 28/09/2026, 10:33:17
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8
9        if not head or left == right:
10            return head
11
12        # Node before left
13        before_left = None
14
15        # Find left position
16        curr = head
17        count = 1
18
19        while count < left:
20            before_left = curr
21            curr = curr.next
22            count += 1
23
24        # curr = left node
25        left_node = curr
26
27        # Reverse from left to right
28        prev = None
29
30        while count <= right:
31            nxt = curr.next
32
33            curr.next = prev
34            prev = curr
35            curr = nxt
36
37            count += 1
38
39        # prev = right node
40        # curr = node after right
41
42        # Connect node before left -> right
43        if before_left:
44            before_left.next = prev
45        else:
46            head = prev
47
48        # Connect left node -> node after right
49        left_node.next = curr
50
51        return head