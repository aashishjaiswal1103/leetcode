# Last updated: 14/10/2026, 12:52:04
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
9        
10        ans = []
11        queue =deque([root])
12        while queue:
13            size = len(queue)
14            total = 0 
15            for _ in range(size):
16                node  = queue.popleft()
17                total+=node.val
18                if node.left:
19                    queue.append(node.left)
20                if node.right :
21                    queue.append(node.right)
22            ans.append(total/size)
23        return ans 
24            
25            
26
27
28
29