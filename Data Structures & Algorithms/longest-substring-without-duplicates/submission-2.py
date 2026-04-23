class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        length = 0
        left = 0

        for right,val in enumerate(s):
            if val in char_map and char_map[val] >= left:
                left = char_map[val] + 1
            char_map[val] = right
            length = max(length,right - left + 1)
        return length