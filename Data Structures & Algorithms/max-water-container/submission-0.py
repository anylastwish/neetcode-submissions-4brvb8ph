class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        max_volume = 0
        while l<r:
            volume = min(heights[l], heights[r])*(r-l)
            max_volume = max(max_volume, volume)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max_volume
