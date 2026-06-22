# Last updated: 22/06/2026, 20:54:01
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic1 ={}
        for ch in s :
            if ch not in dic1 :
                dic1[ch] = 1
            else :
                dic1[ch] +=1
        for ch in t :
            if ch in dic1 :
                dic1[ch] -= 1 
            else :return False 
        if all(value == 0 for value in dic1.values()):
            return True
        else :return False