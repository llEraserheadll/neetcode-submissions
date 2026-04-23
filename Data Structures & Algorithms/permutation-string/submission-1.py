class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26

        len1 = len(s1)
        len2 = len(s2)

        for s in s1:
            s1_count[ord(s)-ord('a')] += 1
        
        for i in range(len2):

            s2_count[ord(s2[i]) - ord('a')] += 1

            if i >= len1:
                s2_count[ord(s2[i-len1]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
        
        return False