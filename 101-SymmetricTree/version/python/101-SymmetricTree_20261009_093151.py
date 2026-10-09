# Last updated: 09/10/2026, 09:31:51
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        def check(nodep, nodeq):
10
11            if nodep is None and nodeq is None:
12                return True
13
14            if nodep is None or nodeq is None:
15                return False
16
17            if nodep.val != nodeq.val:
18                return False
19
20            return check(nodep.left, nodeq.right) and \
21                   check(nodep.right, nodeq.left)
22        if not root :
23            return True 
24        return check(root.left , root.right)
25 
26        