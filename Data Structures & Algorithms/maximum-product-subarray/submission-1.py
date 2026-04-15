class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 
        
        maxProduct = nums[0]
        minProduct = nums[0]
        res = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num<0:
                maxProduct,minProduct = minProduct, maxProduct
            maxProduct = max(num, num*maxProduct)
            minProduct = min(num, num*minProduct)
            res = max(res, maxProduct)
        return res

