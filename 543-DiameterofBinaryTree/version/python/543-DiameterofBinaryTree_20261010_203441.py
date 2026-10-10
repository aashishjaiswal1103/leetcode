# Last updated: 10/10/2026, 20:34:41
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        D  = 0 
10        def dfs(node ):
11            nonlocal D
12            if node is None :
13                return 0 
14            L = dfs(node.left)
15            R = dfs(node.right)
16            D = max(D , L+R)
17            return max(L, R) + 1
18        dfs(root)
19        return D
20
21        