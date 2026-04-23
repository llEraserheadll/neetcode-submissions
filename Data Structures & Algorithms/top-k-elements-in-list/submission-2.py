class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        res = []

        for num,cnt in map.items():
            arr[cnt].append(num)

        
        for i in range(len(arr) - 1,0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
