# Last updated: 03/10/2026, 14:40:37
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next= head 
10        curr= dummy
11        while curr:
12            if curr.next and curr.next.val >=5:
13                curr.val = (curr.val*2 +1)%10
14            elif curr.next is None  or curr.next.val<5:
15                curr.val = (curr.val*2)%10
16            curr=curr.next
17        if dummy.val==0:
18            return dummy.next
19        else:
20            return dummy
21