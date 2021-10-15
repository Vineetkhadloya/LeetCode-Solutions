# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = collections.deque()
        
        # Add root node to queue
        q.append(root)
        
        # Iterate till queue is not empty
        while q:
            level = []
            
            # find qLen to just pop nodes at current level
            qLen = len(q)
            
            # pop current level nodes from queue and append their children
            for i in range(qLen):
                n = q.popleft()
                # Add node only if it is not null
                # Will be null when leaf node children are encountered
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            
            # Append level only if it has values
            # At last level i.e at leaf nodes next level would be null
            if level:
                res.append(level)
        
        return res