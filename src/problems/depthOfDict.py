# Return dept of Dictionary

def dict_depth1(dic, level = 1):
      
    if not isinstance(dic, dict) or not dic:
        return level
    return max(dict_depth1(dic[key], level + 1)
                               for key in dic)

def dict_depth2(myDict):
  
    Ddepth = 1
    obj = [(k, Ddepth + 1) for k in myDict.values()
                          if isinstance(k, dict)]
    max_depth = 0
      
    while(obj):
        n, Ddepth = obj.pop()
        max_depth = max(max_depth, Ddepth)
          
        obj = obj + [(k, Ddepth + 1) for k in n.values()
                                 if isinstance(k, dict)]
          
    return max_depth
      
# # Driver code 
# myDict = {1:{4:{3:3}}, 2: {3: {4:{}}}}
myDict = {4:{2:4}}
print(dict_depth1(myDict))
print(dict_depth2(myDict))