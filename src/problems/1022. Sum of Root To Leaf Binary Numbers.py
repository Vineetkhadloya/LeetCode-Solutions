# You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def dfs(root,path,res):
            
            # Add value of current node to path
            path += (str(root.val))
            
            # If node does not have children then we have reached leaf node and we convert that path to int 
            if (not root.left and not root.right):
                res[0] += int(path,2)
                return
            # If left child exists then proceed to that part
            if root.left :
                dfs(root.left,path,res)
            # If right child exists then proceed to that part
            if root.right:
                dfs(root.right,path,res)
            
        dfs(root,"",res)
        
        return res[0]