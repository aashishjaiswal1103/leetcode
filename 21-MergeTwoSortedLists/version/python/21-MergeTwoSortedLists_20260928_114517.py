# Last updated: 28/09/2026, 11:45:17
1class Solution:
2    def mergeTwoLists(self, list1, list2):
3        
4        dummy = ListNode(-1)
5        tail = dummy
6        
7        while list1 and list2:
8            
9            if list1.val <= list2.val:
10                tail.next = list1
11                list1 = list1.next
12            else:
13                tail.next = list2
14                list2 = list2.next
15            
16            tail = tail.next
17        
18        # attach remaining nodes
19        if list1:
20            tail.next = list1
21        else:
22            tail.next = list2
23        
24        return dummy.next
25        