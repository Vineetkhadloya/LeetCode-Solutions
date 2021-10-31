# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root :
                return [0,True]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            isBalFromRoot = (abs(left[0] - right[0]) <= 1)
            # heightDiff = abs(left[0] - right[0])
            # if heightDiff <= 1 :
            #     isBalFromRoot = True
            # else:
            #     isBalFromRoot = False
            
            areSubTreesBalanced = left[1] and right[1]
            
            return([1 + max(left[0],right[0]), isBalFromRoot and areSubTreesBalanced])
            
            
        return dfs(root)[1]
            