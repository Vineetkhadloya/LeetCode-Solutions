# Given the root of a binary tree, return the maximum path sum of any path.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # Initialize result with value of root node
        res = [root.val]
        
        # Peforming DFS on tree to find max path
        def dfs(root): 
            # If leaf node is reached then its left and right child would be null
            if not root:
                return 0
            
            # Perform DFS on left and right child
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # If value of path is negative then return 0
            leftMax = max(leftMax,0)
            rightMax = max(rightMax,0)
            
            # Calculate result with path split at that node
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # Return value of maximum path
            return root.val + max(leftMax,rightMax)
        
        dfs(root)
        return res[0]