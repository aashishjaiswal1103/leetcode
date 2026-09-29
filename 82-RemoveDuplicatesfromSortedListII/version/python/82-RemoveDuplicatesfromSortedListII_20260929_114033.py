# Last updated: 29/09/2026, 11:40:33
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
8        dummy = ListNode(-1)
9        dummy.next=head 
10
11        curr= head
12        prev= dummy 
13        while curr is not None :
14            if  curr.next is not None  and curr.val==curr.next.val:
15                while curr.next is not None  and curr.val==curr.next.val:
16                    curr = curr.next
17                prev.next = curr.next 
18            else :
19                prev= prev.next 
20            curr= curr.next 
21        return dummy.next 