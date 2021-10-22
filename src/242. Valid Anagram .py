# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        Smap = {}
        Tmap = {}
        for i in range(len(s)):
            Smap.update({s[i]:Smap.get(s[i],0)+1})
            Tmap.update({t[i]:Tmap.get(t[i],0)+1})
            
        for i in Smap:
            if(Smap[i] != Tmap.get(i,0)):
                return False
            
        return True
    
        # Another Approach
        return (sorted(s) == sorted(t))