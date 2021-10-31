# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Maintain set of words encountered so far
        w = set()
        res = 0
        l = 0
        
        # Maintaining window of only unique elements and checking length in every iteration
        for r in range(len(s)):
            while(s[r] in w):
                w.remove(s[l])
                l += 1
                
            w.add(s[r])
            res = max(res,len(w))

        return res