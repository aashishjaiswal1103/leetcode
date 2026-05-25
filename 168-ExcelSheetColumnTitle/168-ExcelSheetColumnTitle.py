# Last updated: 25/05/2026, 21:51:48
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        n = columnNumber
        while n>0:
            remainder = n%26 
            if remainder==0:
                last = 'Z'
                n=(n//26)-1
            else:
                last = chr(ord('A')+remainder-1)
                n=n//26
            result = last + result 
        return result 
        