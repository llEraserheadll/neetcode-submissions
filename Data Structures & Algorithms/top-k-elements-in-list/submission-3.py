import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        unique = list(map.keys())


        def frequency(left,right,index):
            pivot_freq = map[unique[index]]
            unique[right],unique[index] = unique[index],unique[right]
            store = left

            for i in range(left,right):
                if map[unique[i]] > pivot_freq:
                    unique[i],unique[store] = unique[store],unique[i]
                    store += 1
            
            unique[store],unique[right] = unique[right],unique[store]

            return store


        def quickselect(l,r,kth):
            if l >= r:
                return
            
            pivot_index = random.randint(l,r)
            pivot_index = frequency(l,r,pivot_index)

            if kth == pivot_index:
                return
            elif pivot_index > kth:
                quickselect(l,pivot_index - 1,kth)
            else:
                quickselect(pivot_index+1,r,kth)




        quickselect(0,len(unique) - 1,k-1)

        return unique[:k]