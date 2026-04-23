from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        
        left = 0
        res_len = float('inf')
        result = [0,0]
        

        freq_map = Counter(t)
        window = {}
        window_size = 0
        required = len(freq_map)
        current = 0

        for right in range(len(s)):
            right_char = s[right]
            if right_char in freq_map :
                if right_char in window:
                    window[right_char] += 1
                else:
                    window[right_char] = 1
                
                if window[right_char] == freq_map[right_char]:
                    current += 1
                
                while current == required:
                    if right - left + 1 < res_len:
                        result = [left,right]
                        res_len = right - left + 1
                    
                    left_char = s[left]

                    if left_char in freq_map:
                        window[left_char] -= 1

                        if window[left_char] < freq_map[left_char]:
                            current -= 1

                    left += 1
            
        return s[result[0]:result[1] + 1] if res_len != float('inf') else ''



