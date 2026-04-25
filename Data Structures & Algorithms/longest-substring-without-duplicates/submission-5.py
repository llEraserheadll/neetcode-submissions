class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        map = {}
        longest = 0

        for right,char in enumerate(s):
            if char in map and map[char] >= left:
                left = 1 + map[char]
            
            map[char] = right

            longest = max(longest,right - left + 1)
        return longest
