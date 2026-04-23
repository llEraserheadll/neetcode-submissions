from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = Counter(nums)

        for val in map.values():
            if val > 1:
                return True
        return False