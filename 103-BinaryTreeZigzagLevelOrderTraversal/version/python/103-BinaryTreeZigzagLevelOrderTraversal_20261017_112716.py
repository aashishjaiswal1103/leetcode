# Last updated: 17/10/2026, 11:27:16
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
9        if  root is None:
10            return []
11        ans = []
12        queue = deque([root])
13        flag = False 
14
15        while queue :
16            size = len(queue)
17            level =[]
18            for _ in range(size):
19                node = queue.popleft()
20                level.append(node.val)
21                
22                if node.left:
23                    queue.append(node.left)
24                if node.right:
25                    queue.append(node.right)
26            if flag:
27                level.reverse()
28                flag = False
29            else:
30                flag = True 
31            ans.append(level)
32        return ans
33
34
35
36
37        