class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2

        #A is the shorter array
        left = 0
        right = len(A) - 1

        while True:
            Amid = (left + right) // 2
            Bmid = half - Amid - 2

            Aleft = A[Amid] if Amid >= 0 else float('-infinity')
            Aright = A[Amid + 1] if Amid + 1 < len(A) else float('infinity')
            Bleft = B[Bmid] if Bmid >= 0 else float('-infinity') 
            Bright = B[Bmid + 1] if Bmid + 1<len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/ 2.0
            elif Aleft > Bright:
                right = Amid - 1
            else:
                left = Amid + 1