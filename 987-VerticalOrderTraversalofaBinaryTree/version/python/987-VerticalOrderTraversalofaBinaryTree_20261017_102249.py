# Last updated: 17/10/2026, 10:22:49
1class Solution:
2    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
3        pair = []
4        groups = {}
5
6        def level(node, column, row):
7            if node is None:
8                return
9
10            pair.append(((node.val, column), row))
11
12            level(node.left, column - 1, row + 1)
13            level(node.right, column + 1, row + 1)
14
15        level(root, 0, 0)
16
17        pair.sort(key=lambda x: (x[0][1], x[1], x[0][0]))
18
19        for ((key, column), row) in pair:
20            groups.setdefault(column, []).append(key)
21
22        ans = [groups[column] for column in sorted(groups)]
23
24        return ans