# Last updated: 29/09/2026, 11:43:05
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
8        if head is None or head.next is None:
9            return head
10            
11        dummy = ListNode(-1)
12        dummy.next=head 
13
14        curr= head
15        prev= dummy 
16        while curr is not None :
17            if  curr.next is not None  and curr.val==curr.next.val:
18                while curr.next is not None  and curr.val==curr.next.val:
19                    curr = curr.next
20                prev.next = curr.next 
21            else :
22                prev= prev.next 
23            curr= curr.next 
24        return dummy.next 