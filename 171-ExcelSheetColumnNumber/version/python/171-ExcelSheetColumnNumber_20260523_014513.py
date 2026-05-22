# Last updated: 23/05/2026, 01:45:13
1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        result = 0 
4        for ch in columnTitle:
5            value = ord(ch)- 64
6            result = 26*result+value
7        return result 