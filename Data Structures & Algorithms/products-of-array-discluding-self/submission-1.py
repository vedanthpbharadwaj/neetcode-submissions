class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """prefix = 1
        suffix = 1
        right = []
        left = []

        for num in nums:
            left.append(prefix)
            prefix *= num

        for num in reversed(nums):
            right.append(suffix)
            suffix *= num

        right.reverse()

        answer = []
        for i in range(len(nums)):
            answer.append(right[i]*left[i])

        return answer"""


        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1): # reversing the list and traversing from the last
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
        