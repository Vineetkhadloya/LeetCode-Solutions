# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

# Maintain a window of the range which current postion can cover
# Check which element in the window can take us the farthest and update r with that value
# now check window from old(r)+1 to new r
# increment jump with each iteration
class Solution:
    def jump(self, nums: List[int]) -> int:

        l = r = 0
        farthest = 0
        j = 0
        
        while r < len(nums)-1:
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            l = r+1
            r = farthest
            j += 1
            
        return j