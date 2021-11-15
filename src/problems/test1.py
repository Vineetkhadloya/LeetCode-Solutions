def dict_depth(dic,level = 1):
    print("dic = "+str(dic))
    if not isinstance(dic,dict) or not dic:
        print("returning level = "+str(level))
        return level

    for key in dic:
        if isinstance(dic[key],dict):
            print("calling = ",dic[key])
            res[0] = max(res[0],dict_depth(dic[key],level+1))
        else:
            res[0] = max(res[0],level)

    print("returning res[0] = "+str(res[0]))
    return res[0]

res = [0]
myDict = {2:{}}
print("my dict = " + str(myDict))
# myDict = {1:'Geek', 2: {3: {4: {}}}}
print(dict_depth(myDict))