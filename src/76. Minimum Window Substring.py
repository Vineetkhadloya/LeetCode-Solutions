# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Maintain hashmap of string t
        tMap = {}
        # Maintain hashmap of charcters in window
        wMap = {}
        
        l = 0
        res = [-1,-1]
        resLen = float("inf")
        
        # Add chracters if string t in Hashmap
        for i in t:
            tMap.update({i:tMap.get(i,0)+1})
        
        # req is to check if our window has all characters in t
        req = len(tMap)
        # have keeps track of characters in window which are in t
        have = 0
        
        # Traverse through the string s
        for r in range(len(s)):
            # Add character to windowMap
            wMap.update({s[r]:wMap.get(s[r],0)+1})
            
            # If character also in t and no. of that char req is satisfied we increment have by 1
            if(s[r] in tMap and wMap[s[r]] == tMap[s[r]]) : 
                have += 1
            
            # If have == req this means our window now has all required characters
            # Till this condition is satisfied decrement window from left side
            while have == req:

                if((r-l+1) < resLen):
                    res = [l,r]
                    resLen = r-l+1
                
                wMap[s[l]] -= 1
                if(s[l] in tMap and wMap[s[l]] < tMap[s[l]]):
                    have -= 1
                l += 1
        
        l,r = res
        return "" if resLen == float("inf") else s[l:r+1]