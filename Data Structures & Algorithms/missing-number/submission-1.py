class Solution:
    def missingNumber(self, nums: List[int]) -> nums:
        n = len(nums)
        total = n*(n +1)//2
        for num in nums:
            total -= num
        return total