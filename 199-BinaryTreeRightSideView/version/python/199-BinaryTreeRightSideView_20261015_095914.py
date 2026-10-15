# Last updated: 15/10/2026, 09:59:14
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: TreeNode | None) -> list[int]:
9        if root is None :
10            return []
11        queue =deque([root])
12        ans=[]
13        
14        while queue:
15            size = len(queue)
16            count = 0
17            for _ in range(size):
18                count+=1
19                if count == size :
20                    node = queue.popleft()
21                    ans.append(node.val)
22
23                    if node.left:
24                        queue.append(node.left)
25                    if node.right :
26                        queue.append(node.right)
27                else :
28                    node = queue.popleft()
29                    if node.left:
30                        queue.append(node.left)
31                    if node.right :
32                        queue.append(node.right)
33        return ans 
34
35
36                 
37        