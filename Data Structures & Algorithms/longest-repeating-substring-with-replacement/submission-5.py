class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        char_map = {}
        max_freq = 0
        substr_len = 0


        for right in range(len(s)):
            if s[right] in char_map:
                char_map[s[right]] += 1
            else:
                char_map[s[right]] = 1
            

            max_freq = max(max_freq,char_map[s[right]])

            if right - left + 1 - max_freq > k:
                char_map[s[left]] -= 1
                left += 1
            
            substr_len = max(substr_len,right - left + 1)
        
        return substr_len