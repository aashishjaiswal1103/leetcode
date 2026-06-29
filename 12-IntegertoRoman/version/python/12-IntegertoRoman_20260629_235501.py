# Last updated: 29/06/2026, 23:55:01
# using dictionary  and divison to find the value and key form dict
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        roman = { 1000: "M", 900: "CM", 500: "D",400: "CD",100: "C",90: "XC",50: "L",40: "XL",10:"X",9: "IX",5: "V",4: "IV",1: "I"}
4
5        ans = []
6
7        for value, symbol in roman.items():
8            count = num // value
9            ans.append(symbol * count)
10            num %= value
11
12        return "".join(ans)