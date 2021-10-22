# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        # Start from left to right
        # Calculate the product of numbers before an index and store that value in res at that index
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        # Start from right to left
        # Calculate the product of numbers after an index and multiply it with existing value in res at that index
        # These 2 calculation will give the product of numbers before and after the index 
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = postfix * res[i]
            postfix = postfix * nums[i]
            
        return res