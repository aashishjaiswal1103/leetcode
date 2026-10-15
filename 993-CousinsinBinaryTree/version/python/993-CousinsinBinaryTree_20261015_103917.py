# Last updated: 15/10/2026, 10:39:17
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
9        queue= deque([root])
10        while queue:
11            flag  = False 
12            size = len(queue)
13            for _ in range(size):
14                node = queue.popleft()
15                if node.left and node.right:
16                    if (node.left.val==x and node.right.val==y) or (node.left.val==y and node.right.val==x):
17                        return False 
18                if node.left:
19                    queue.append(node.left)
20                if node.right:
21                    queue.append(node.right)
22                if (node.val == x or node.val==y)  and  not flag :
23                    flag =True 
24                    if node.val == x :
25                        x=0
26                    if node.val ==y :
27                        y=0
28                if (node.val == x or node.val==y)  and  flag :
29                    return True 
30        return False 
31
32
33        