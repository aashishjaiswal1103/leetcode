# Last updated: 26/05/2026, 00:49:38
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        m=[]
        for i in range(numRows):
            m.append([0]*(i+1))
            for j in range(i+1):
                if i>1:
                    if j ==0 or j==i:
                        m[i][j]=1
                    else: 
                        m[i][j]=m[i-1][j-1]+m[i-1][j]
                    
                else:
                    m[i][j]=1
        return m 