# Last updated: 15/05/2026, 11:45:11
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for name, _ in sorted(zip(names, heights), key=lambda x: -x[1])]