class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastind = {}
        size = end = 0
        res = []

        for i,c in enumerate(s):
            lastind[c] = i
        
        for i in range(len(s)):
            end = max(end,lastind[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res

