import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        unique = list(freq.keys())
        n = len(unique) - 1

        def partition(left,right,pivot_index):
            pivot_freq = freq[unique[pivot_index]]
            unique[right],unique[pivot_index] = unique[pivot_index],unique[right]
            store = left

            for i in range(left,right):
                if freq[unique[i]] > pivot_freq:
                    unique[store],unique[i] = unique[i],unique[store]
                    store += 1
            
            unique[store],unique[right] = unique[right],unique[store]

            return store


        def quickselect(left,right,kth):
            pivot_index = random.randint(left,right)
            pivot_index = partition(left,right,pivot_index)

            if pivot_index == kth:
                return
            elif pivot_index > kth:
                quickselect(left,pivot_index - 1,kth)
            else:
                quickselect(pivot_index+1,right,kth)

        quickselect(0,n,k-1)
        return unique[:k]