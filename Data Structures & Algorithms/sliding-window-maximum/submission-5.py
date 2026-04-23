class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        output = []

        for index,val in enumerate(nums):
            if dq and index-k == dq[0]:
                dq.popleft()
            
            while dq and val > nums[dq[-1]]:
                dq.pop()
            
            dq.append(index)

            if index >= k-1:
                output.append(nums[dq[0]])
        
        return output