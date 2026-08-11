# Last updated: 11/08/2026, 16:19:42
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        st = re.sub(r'[^a-zA-Z0-9]', '', s)
4        sk = st.lower()
5
6        x = 0
7        n = len(sk) - 1
8
9        def pal(x, n):
10            if x >= n:
11                return True
12
13            if sk[x] != sk[n]:
14                return False
15
16            return pal(x + 1, n - 1)
17
18        return pal(x, n)