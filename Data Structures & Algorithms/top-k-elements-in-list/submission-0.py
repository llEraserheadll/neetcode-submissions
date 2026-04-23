import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        unique = list(freq.keys())
        length = len(unique) - 1



        def partition(left,right,pivot_index):
            pivot_freq = freq[unique[pivot_index]]

            unique[pivot_index],unique[right] = unique[right],unique[pivot_index]
            store = left

            for i in range(left,right):
                if freq[unique[i]] > pivot_freq:
                    unique[store],unique[i] = unique[i],unique[store]
                    store += 1
            
            unique[right],unique[store] = unique[store],unique[right]

            return store

        
        def quickselect(left,right,kth_freq):
            if left >= right:
                return
            
            pivot_index = random.randint(left,right)
            pivot_index = partition(left,right,pivot_index)

            if pivot_index == kth_freq:
                return 
            elif pivot_index > kth_freq:
                quickselect(left,pivot_index- 1,kth_freq)
            else:
                quickselect(pivot_index + 1,right,kth_freq)

        quickselect(0,length,k - 1)
        return unique[:k]

