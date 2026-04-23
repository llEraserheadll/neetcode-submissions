class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26 

        ns1 = len(s1)
        ns2 = len(s2)

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        for i in range(ns2):
            s2_count[ord(s2[i]) - ord('a')] += 1

            if i >= ns1:
                s2_count[ord(s2[i-ns1]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True

        return False 