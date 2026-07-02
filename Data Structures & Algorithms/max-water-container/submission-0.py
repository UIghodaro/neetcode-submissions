class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most, current = 0, 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            if heights[left] < heights[right]:
                current = heights[left]*(right-left)
                left += 1
            else:
                current = heights[right]*(right-left)
                right -= 1
            
            if current > most:
                most = current

        
        return most
            

