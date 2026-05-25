# Last updated: 25/05/2026, 21:51:49
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0 
        for ch in columnTitle:
            value = ord(ch)- 64
            result = 26*result+value
        return result 