class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        write = 0

        for x in nums:
            if x != 0:
                nums[write] = x
                write += 1

        while write < len(nums):
            nums[write] = 0
            write += 1
            