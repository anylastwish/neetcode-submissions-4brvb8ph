class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        prev2 = nums[0]
        prev1 = max(prev2, nums[1])
        for i in range(2, len(nums)-1):
            curr = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = curr
        maxCost1 = prev1

        prev2 = nums[1]
        prev1 = max(prev2, nums[2])
        for i in range(3, len(nums)):
            curr = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = curr
        return max(maxCost1, prev1)
