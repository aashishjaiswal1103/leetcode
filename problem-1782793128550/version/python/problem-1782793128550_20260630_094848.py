# Last updated: 30/06/2026, 09:48:48
# basic prob
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        ans = []
4        for i in range(1,n+1):
5            
6         
7            if i%3==0 and i%5==0:
8                ans.append("FizzBuzz")
9            elif i%3==0 :
10                ans.append("Fizz")
11            elif i%5 ==0 :
12                ans.append("Buzz")
13            else :
14                ans.append(str(i))
15        return ans
16