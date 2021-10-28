# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Dynamic Programming Bottom Up approach
        dp = [False] * (len(s) + 1)
        
        # Last cell in dp represents empty string which will always be true
        dp[-1] = True
        
        # Start checking from end of string
        for i in range(len(s),-1,-1):
            # Compare characters in scope with words in dictionary
            for w in wordDict:
                # If word is found then update value at position where word is starting with 
                # value of position after word is ending to ensure remaining characters also correspond
                # to a word in the dictionary
                if(len(s)-i >= len(w) and s[i:i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                    
                if(dp[i] == True) :
                    break
            
        return dp[0]