# Last updated: 10/10/2026, 11:09:12
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
9        #usign the dfs approach
10        ans = []
11        def dfs(node , level):
12            if node is None:
13                return 
14            if level ==len(ans):
15                ans.append([])
16            ans[level].append(node.val)
17            dfs(node.left , level + 1 )
18            dfs(node.right , level + 1)
19        dfs(root,0)
20        return ans
21        