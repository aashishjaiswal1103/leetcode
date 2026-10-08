# Last updated: 08/10/2026, 11:48:42
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9        ans = []
10        def preorder(node):
11            if node == None:
12                return 
13            preorder(node.left)
14            ans.append(node.val)
15            preorder(node.right)
16        preorder(root)
17        return ans 
18        