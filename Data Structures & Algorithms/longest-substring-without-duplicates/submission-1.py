class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        char_map = {}

        for right,val in enumerate(s):
            if val in char_map and char_map[val] >= left:
                left = char_map[val] + 1
            
            char_map[val] = right

            longest = max(longest,right - left + 1)
        
        return longest