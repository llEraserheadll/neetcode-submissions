class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_map = Counter(nums)

        for val,freq in freq_map.items():
            if freq > 1:
                return val