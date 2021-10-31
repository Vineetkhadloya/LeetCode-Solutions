# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            
            # Base Case : If leaf node encountered : return 0
            if not node:
                return 0
            
            # If node value is greater than maxNode encountered in path then it will become 1
            rootVal = node.val >= maxVal
            
            # Update MaxValue by comparing with current node
            maxVal = max(maxVal,node.val)
            
            # Recursively call left child and right child
            leftVal = dfs(node.left,maxVal)
            rightVal = dfs(node.right,maxVal)
            
            return rootVal + leftVal + rightVal
        
        return dfs(root,root.val)

# Sol 2

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = [0]
        def dfs(root,maxVal):
            
            if not root:
                return 0
            
            if(root.val >= maxVal):
                res[0] += 1
                maxVal = root.val
                
            dfs(root.left,maxVal)
            dfs(root.right,maxVal)
            
        dfs(root,root.val)
        return res[0]