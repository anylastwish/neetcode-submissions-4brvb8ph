class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in seen_map:
                return [seen_map[remaining], i]
            seen_map[n] = i
        