# Last updated: 21/10/2026, 09:21:03
1from collections import deque
2
3class Solution:
4    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
5        if not root:
6            return root
7
8        queue = deque([root])
9
10        while queue:
11            size = len(queue)
12
13            for i in range(size):
14                node = queue.popleft()
15
16                if i == size - 1:
17                    node.next = None
18                else:
19                    node.next = queue[0]
20
21                if node.left:
22                    queue.append(node.left)
23                if node.right:
24                    queue.append(node.right)
25
26        return root