# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# We keep track of Current Maximum and Current Minimum as when there are even number of negative numbers in our consecutive subarray without zero then with current minimum we can get maximum value up until that point including previous encountered negative number
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        
        curMax = 1
        curMin = 1
        
        for i in nums:
            if i == 0:
                curMax = 1
                curMin = 1
                res = max(res,i)
                continue
            
            t = curMax * i
            curMax = max(t, curMin*i, i)
            curMin = min(t, curMin*i, i)

            res = max(res,curMax)
            
        return res