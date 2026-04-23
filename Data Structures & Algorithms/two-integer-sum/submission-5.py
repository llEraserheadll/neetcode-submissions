class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index,val in enumerate(nums):
            diff = target - val
            if diff in map:
                return [map[diff],index]
            map[val] = index