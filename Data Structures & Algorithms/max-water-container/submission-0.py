class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxima = 0
        left = 0
        right = len(heights)-1
        while left < right:
            if (right - left) * min(heights[left], heights[right]) > maxima:
                maxima = (right - left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxima