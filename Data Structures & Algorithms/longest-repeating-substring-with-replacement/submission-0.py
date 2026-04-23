class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        n = len(s)

        substr_length = 0
        max_freq = 0
        start = 0

        for end in range(n):
            if s[end] not in freq:
                freq[s[end]] = 1
            else:
                freq[s[end]] += 1
            
            max_freq = max(max_freq,freq[s[end]])

            if end - start + 1 - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            
            substr_length = max(substr_length,end - start + 1)
        
        return substr_length