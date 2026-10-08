# Last updated: 08/10/2026, 12:08:17
1class Solution:
2    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
3
4        def check(nodep, nodeq):
5
6            if nodep is None and nodeq is None:
7                return True
8
9            if nodep is None or nodeq is None:
10                return False
11
12            if nodep.val != nodeq.val:
13                return False
14
15            return check(nodep.left, nodeq.left) and \
16                   check(nodep.right, nodeq.right)
17
18        return check(p, q)