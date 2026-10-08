# Last updated: 08/10/2026, 11:46:30
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
9        ans = []
10        
11        def preorder(node):
12            if node == None:
13                return 
14            ans.append(node.val)
15            preorder(node.left)
16            preorder(node.right)
17        preorder(root)
18        return ans 
19                