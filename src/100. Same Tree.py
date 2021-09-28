# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If both trees are null then they are same
        if not p and not q:
            return True
        
        # Check if one of the tree is null
        # Check if value of root node of p == root node of q
        if (not p or not q) or (p.val != q.val):
            return False
        
        # Recursilvely call isSameTree Function with left and right children
        return (self.isSameTree(p.left,q.left) or self.isSameTree(p.right,q.right))
        
        
        