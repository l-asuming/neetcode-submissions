class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            h = min(heights[i], heights[j])
            w = j - i
            area = max(area,w*h)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return area




        