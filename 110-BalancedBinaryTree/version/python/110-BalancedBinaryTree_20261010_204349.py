# Last updated: 10/10/2026, 20:43:49
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: TreeNode | None) -> bool:
9        d=True
10        def balance(node):
11            nonlocal d
12            if node is None :
13                return 0 
14            l = balance(node.left)
15            r=  balance(node.right)
16            if abs(l-r)>1:
17                d=False 
18            return max(l,r)+1 
19        
20        balance(root)
21        return d 