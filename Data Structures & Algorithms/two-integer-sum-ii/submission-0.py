class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = len(numbers)
        r = n-1
        while l<r:
            if target == numbers[l]+numbers[r]:
                return [l+1, r+1]
            elif target > numbers[l]+numbers[r]:
                l+=1
            else:
                r-=1
        return []
        