# Last updated: 02/10/2026, 10:36:43
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        curr = head 
13        dummy = Node(0)
14        head2 = dummy 
15        dummy.next = None 
16         
17        # Create the copied linked list
18        while curr:
19            v = curr.val 
20            curr2 = Node(v)
21
22            head2.next = curr2
23            head2 = head2.next
24
25            curr = curr.next 
26
27        # Now copy the random pointers
28        curr = head
29        curr2 = dummy.next 
30
31        while curr:
32            if curr.random != None:
33                
34                head2 = head
35                copy2 = dummy.next
36
37                while head2:
38                    if head2 == curr.random:
39                        curr2.random = copy2
40                        break
41                    else:
42                        head2 = head2.next
43                        copy2 = copy2.next
44
45            else:
46                curr2.random = None
47
48            curr = curr.next
49            curr2 = curr2.next
50
51        return dummy.next    