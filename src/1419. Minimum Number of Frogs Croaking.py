# You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

# Return the minimum number of different frogs to finish all the croaks in the given string.

# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        # maintaining this list to get previous character 
        c = ['c','r','o','a','k']
        
        # Keeps track of current ongoing croaks
        croakCount = 0
        
        # Keeps track of maximum croaks so far
        op = 0
        
        # Keeps count of characters 
        cMap = {}
        
        # Iterating through Input String
        for i in croakOfFrogs:
            
            # Incrementing counter of character if it is not k i.e last character
            if i != "k" :
                cMap[i] = cMap.get(i,0) + 1
            # If character is k then we decrement number of active croaks by 1
            else:
                croakCount -= 1
            
            # Getting what the previous character of current character is in "croak"
            prevChar = c[c.index(i) - 1]
            
            # If chracter is c we increment current active croak counter by 1 and update op if current count is max
            if i == "c" : 
                croakCount+=1
                op = max(op,croakCount)
            # If it is any other element than c then we check if the occurance of "prevChar" should be greater than 0
            # If it is not greater than zero this indicates invalid string
            elif cMap.get(prevChar,0) <= 0 :
                return -1
            # We decrement count of previous character by one as this will be part of string curresponding to current character
            else:
                cMap[prevChar] -= 1
            
        # If active croakCount is not zero we have an incomplete croak and it is an invalid scenario
        if croakCount != 0 :
            return -1
        else:
            return op
        
