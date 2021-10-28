nums=[27, 29, 35, 42]
nums_len = len(nums)
if nums_len == 0:
	print(nums)
elif nums_len == 1:
	print(nums[0])
elif nums_len >= 2 and nums[0]<nums[nums_len-1]:
	print(nums[nums_len-1])
else:
    left, right = 0, nums_len-1
    while left < right:
    	if (right - left)==1:
    	    print(nums[left])
    	    break
    	mid = left + (right-left)//2
    	if nums[mid]>nums[left]:
    		left = mid
    	elif nums[mid]<nums[left]:
    		right = mid