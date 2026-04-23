class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        window = {}
        max_freq = 0


        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1
            
            max_freq = max(max_freq,window[s[right]])

            if right - left + 1 - max_freq > k:
                window[s[left]] -= 1
                left += 1
            
            max_len = max(max_len,right - left + 1)
        
        return max_len

