# Last updated: 26/06/2026, 23:01:34
# sliding window +dictonary to count the most 2 fruite
1from typing import List
2
3class Solution:
4    def totalFruit(self, fruits: List[int]) -> int:
5        left = 0
6        freq = {}
7        ans = 0
8
9        for right in range(len(fruits)):
10            freq[fruits[right]] = freq.get(fruits[right], 0) + 1
11
12            while len(freq) > 2:
13                freq[fruits[left]] -= 1
14                
15                if freq[fruits[left]] == 0:
16                    del freq[fruits[left]]
17                left += 1
18
19            ans = max(ans, right - left + 1)
20
21        return ans