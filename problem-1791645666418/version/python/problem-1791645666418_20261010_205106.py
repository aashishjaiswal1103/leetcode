# Last updated: 10/10/2026, 20:51:06
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: TreeNode | None) -> int:
9        h=0
10        def depth(node):
11            nonlocal h 
12            if node is None :
13                return 0 
14            l=depth(node.left)
15            r=depth(node.right)
16            h = max(l,r)+1
17            return max(l,r)+1
18        depth(root)
19        return h
20
21        