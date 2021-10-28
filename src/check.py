def findMin(nums) :
                
    l = 0
    r = len(nums) - 1

    if(nums[l]<nums[r] and len(nums)>=2):
        return nums[r]

    res = nums[0]
    
    while l <= r:
        print(l,r)
        # if(nums[l] < nums[r]):
        #     res = max(res,nums[r])
        #     print("nums[r] = ",nums[r])
        #     print("res = ",res)
        #     break

        mid = (l+r) // 2
        print("mid = ",mid)
        if mid == 1 and nums[mid] > nums[mid+1] :
            return nums[mid]
            
        if(nums[mid] >= nums[l]) : 
            l = mid + 1
        else : 
            r = mid - 1
        print(l,r)         
    return res
            
a = [1,2,3,4,5]
a = [12,14,15,2,3,11]
# a = [11,14,5,9,10]
print(findMin(a))