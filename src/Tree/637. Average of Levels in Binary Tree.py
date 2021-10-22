#Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
# Answers within 10-5 of the actual answer will be accepted.

# Similar to Binary Tree level order traversal

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q :
            
            level = []
            qLen = len(q)
            sum = 0
            for i in range(qLen):
                
                n = q.popleft()
                if n:
                    level.append(n.val)
                    sum += n.val
                    q.append(n.left)
                    q.append(n.right)
            
            if level:
                res.append(sum/len(level))
            
        return res