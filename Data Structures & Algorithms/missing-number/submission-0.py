class Solution:
    def missingNumber(self, nums: List[int]) -> nums:
        n=len(nums)
        res = nums[0]
        for i in range(1, n):
            res ^= nums[i]
        
        for i in range(n+1):
            res ^= i
        
        return res