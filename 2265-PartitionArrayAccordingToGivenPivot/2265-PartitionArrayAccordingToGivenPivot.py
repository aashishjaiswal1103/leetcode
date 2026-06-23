# Last updated: 24/06/2026, 00:47:58
class Solution:
    def pivotArray(self, nums: List[int], k: int) -> List[int]:
        s = []
        m=[]
        l=[]
        for ch in nums:
            if ch <k:
                s.append(ch)
            elif ch==k:
                m.append(ch)
            else:
                l.append(ch)
        return s+m+l
        