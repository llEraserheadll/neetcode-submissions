class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            m = (left + right) // 2
            hour = 0

            for p in piles:
                hour += math.ceil(float(p)/m)
            
            if hour <= h:
                res = m
                right = m -1
            else:
                left = m + 1
        return res
