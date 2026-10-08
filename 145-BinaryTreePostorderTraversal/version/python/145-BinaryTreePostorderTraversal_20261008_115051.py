# Last updated: 08/10/2026, 11:50:51
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
9        ans = []
10        def postorder(node):
11            if node == None:
12                return 
13            postorder(node.left)
14            
15            postorder(node.right)
16            ans.append(node.val)
17        postorder(root)
18        return ans 
19        
20        