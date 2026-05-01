class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            total = min(heights[l], heights[r]) * (r - l) 
            result = max(result, total)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return result