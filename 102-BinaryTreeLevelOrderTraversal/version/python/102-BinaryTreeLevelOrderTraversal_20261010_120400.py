# Last updated: 10/10/2026, 12:04:00
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
9        if root is None :
10            return []
11        ans = []
12        queue =deque([root])
13        while queue:
14            size = len(queue)
15            level = []
16            for _ in range(size):
17                node = queue.popleft()
18                level.append(node.val)
19                if node.left:
20                    queue.append(node.left)
21                if node.right:
22                    queue.append(node.right)
23            ans.append(level)
24        return ans
25
26
27
28        