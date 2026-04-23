class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1

        for j in range(len(s2)):
            s2_count[ord(s2[j])-ord('a')] += 1

            if j >= len(s1):
                s2_count[ord(s2[j-len(s1)]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
        return False