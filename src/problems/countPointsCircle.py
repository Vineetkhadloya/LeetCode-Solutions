def countPoints(arr):
    nums = 0
    cs = set()
    for a in arr:
        point = [a[0], a[1]]
        radius = a[2]
        for x in range(-radius, radius+1):
            for y in range(-radius, radius+1):
            	print(x,y)
                if (x*x + y*y) <= (radius*radius):
                    print(x+point[0],y+point[1])
                    cs.add((x+point[0], y+point[1]))
            	print("-------")
    nums = len(cs)
    print(nums)


A = [[3,3,2]]
countPoints(A)