class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for key,val in count.items():
            if val > 1:
                return True
        
        return False