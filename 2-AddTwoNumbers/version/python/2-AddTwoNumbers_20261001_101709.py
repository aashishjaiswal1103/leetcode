# Last updated: 01/10/2026, 10:17:09
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
8        num1=0
9        num2=0
10        count=0
11        dummy=ListNode(-1)
12        curr = dummy 
13        
14        while l1:
15            num1+= l1.val*(10**count)
16            count+=1
17            l1=l1.next
18        count =0
19        while l2:
20            num2+= l2.val*(10**count)
21            count+=1
22            l2=l2.next
23        ans=num1+num2
24        for digit in str(ans):
25            newnode = ListNode(int(digit))
26            newnode.next=curr.next
27            curr.next=newnode 
28        return dummy.next
29
30        