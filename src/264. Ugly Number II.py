 # An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        ugly = [1]
 
        p2 = 0
        p3 = 0
        p5 = 0

        while len(ugly) != n:
            
            u2 = ugly[p2]*2
            u3 = ugly[p3]*3
            u5 = ugly[p5]*5
            
            minN = min(u2,u3,u5)
            ugly.append(minN)
            
            if(minN == u2) : p2 += 1
            if(minN == u3) : p3 += 1
            if(minN == u5) : p5 += 1
         
        return ugly[-1]