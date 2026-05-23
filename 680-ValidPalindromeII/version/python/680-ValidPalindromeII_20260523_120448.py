# Last updated: 23/05/2026, 12:04:48
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        
4        def check(i, j):
5            while i < j:
6                if s[i] != s[j]:
7                    return False
8                i += 1
9                j -= 1
10            return True
11        
12        i, j = 0, len(s) - 1
13
14        while i < j:
15            if s[i] != s[j]:
16                return check(i + 1, j) or check(i, j - 1)
17            i += 1
18            j -= 1
19
20        return True