class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        remaining_numbers = set(nums)
        sequence_length = {}
        maxLength = 0
        for current_num in nums:
            if current_num not in remaining_numbers:
                continue
            sequence_end = current_num
            while sequence_end in remaining_numbers:
                remaining_numbers.remove(sequence_end)
                sequence_end += 1
            
            current_length = (sequence_end - current_num) + sequence_length.get(sequence_end, 0)
            sequence_length[current_num] = current_length
            maxLength = max(maxLength, current_length)

        return maxLength
                