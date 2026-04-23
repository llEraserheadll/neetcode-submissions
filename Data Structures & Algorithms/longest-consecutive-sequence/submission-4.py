class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest  = 0

        for nums in numset:
            if nums - 1 not in numset:
                length = 1

                while nums + length in numset:
                    length += 1
            
                longest = max(longest,length)
        
        return longest