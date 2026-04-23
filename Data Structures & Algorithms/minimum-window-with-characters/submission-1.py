class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        freq_map = Counter(t)
        required = len(freq_map)

        result = [0,0]
        min_len = float('inf')

        window = {}
        current = 0
        left = 0


        for right in range(len(s)):
            right_char = s[right]
            if right_char in freq_map:
                if right_char in window:
                    window[right_char] += 1
                else:
                    window[right_char] = 1
                
                if window[right_char] == freq_map[right_char]:
                    current += 1
                
                while current == required:
                    if right - left + 1 < min_len:
                        result = [left,right]
                        min_len = right - left + 1
                    
                    left_char = s[left]

                    if s[left] in freq_map:
                        window[left_char] -= 1
                    
                        if window[left_char] < freq_map[left_char]:
                            current -= 1
                    
                    left += 1
        
        return s[result[0]:result[1]+1] if min_len != float('inf') else ''


                
