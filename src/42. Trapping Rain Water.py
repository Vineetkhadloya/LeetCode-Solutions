# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Edge Case
        if not height : return 0
        
        # Initialize Right and Left pointers
        l = 0
        r = len(height)-1
        
        # Initialize max left and right values 
        res = 0
        lMax = height[l]
        rMax = height[r]
        
        op = []
        # Traversing through list based on max left and right values
        while l < r:
            if lMax < rMax :
                l += 1
                lMax = max(lMax,height[l])
                res += lMax - height[l]  
                
            else:
                r -= 1
                rMax = max(rMax,height[r])
                res += rMax - height[r]

        return res