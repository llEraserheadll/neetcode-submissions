class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = Counter(t)
        window = {}
        required = len(char_map)
        current = 0
        length = float('INF')
        result = [0,0]
        left = 0


        for right in range(len(s)):
            right_char = s[right]
            if right_char in char_map:
                if right_char in window:
                    window[right_char] += 1
                else:
                    window[right_char] = 1
                
                if char_map[right_char] == window[right_char]:
                    current += 1
                
                while current == required:
                    if right - left + 1 < length:
                        length = right - left + 1
                        result = [left,right]
                    
                    left_char = s[left]

                    if left_char in window:
                        window[left_char] -= 1

                        if window[left_char] < char_map[left_char]:
                            current -= 1
                    left += 1
        
        return s[result[0]:result[1] +1] if length != float('INF') else ""
