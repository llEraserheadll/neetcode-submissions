class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        map = {}
        longest_freq = 0
        length = 0


        for right in range(len(s)):
            if s[right] in map:
                map[s[right]] += 1
            else:
                map[s[right]] = 1
            
            longest_freq = max(longest_freq,map[s[right]])

            if right - left + 1 - longest_freq > k:
                map[s[left]] -= 1
                left += 1
            
            length = max(length,right - left + 1)
        
        return length
