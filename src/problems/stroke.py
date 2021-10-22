def solution(a):
    count = 0

    for i in range(max(a)):
        for j in range(len(a)):
            a[j] -= 1

        l = 0
        r = 0
        
        while r < len(a):
            while l+1 < len(a) and a[l] < 0:
                l += 1
            r = l
            while r+1 < len(a) and a[r] >= 0 :
                r += 1
            
            if l == len(a)-1 and r == len(a)-1 : 
                if(a[l] >= 0):         
                    count += 1
            else:
                count += 1

            l = r = r+1
    return count
        
        
#a = [1,3,2,1,2,1,5,3,3,4,2]
#a = [5,8]
a = [1,1,1,1]
solution(a)