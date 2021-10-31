# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Maintain count of each character in current window
        wCount = {}
        
        l = 0
        res = 0
        
        # Traverse through the string
        for r in range(len(s)):
            wCount.update({s[r]:wCount.get(s[r],0) + 1})
            
            # If len of current window - char with max occurance in window is greater that (k) chars we 
            # can replace this means window has more than k diff char apart from max occured char
            if ((r-l+1) - max(wCount.values()) > k):
                wCount[s[l]] -= 1
                l += 1
            # Update max 
            res = max(res,r-l+1)
            
        return res