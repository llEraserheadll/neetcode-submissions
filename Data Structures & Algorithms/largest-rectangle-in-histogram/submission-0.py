class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0

        for index,height in enumerate(heights):
            start = index
            while stack and stack[-1][0] > height:
                h,i = stack.pop()
                width = index - i
                area = h * width
                max_area = max(max_area,area)
                start = i
            
            stack.append([height,start])
        
        while stack:
            a,b = stack.pop()
            width = n - b
            area = a * width
            max_area = max(max_area,area)
        
        return max_area