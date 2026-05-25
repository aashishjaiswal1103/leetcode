# Last updated: 26/05/2026, 00:33:04
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        m=[]
4        for i in range(numRows):
5            m.append([0]*(i+1))
6            for j in range(i+1):
7                if i>1:
8                    if j ==0 or j==i:
9                        m[i][j]=1
10                    else: 
11                        m[i][j]=m[i-1][j-1]+m[i-1][j]
12                    
13                else:
14                    m[i][j]=1
15        return m 