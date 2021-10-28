# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

#----
# BST Property that left child is smaller than root and right child is larger than root
#----

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        # Base condition : If we reach leaf node
        if not root:
            return None
        
        # If root value is higher than high then we can trim root and its right part
        if(root.val > high):
            return self.trimBST(root.left,low,high)
        # If root value is lower than low then we can trim root and its left part
        if(root.val<low):
            return self.trimBST(root.right,low,high)
        
        # Recursively calling trim on left and right children
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        
        # Return root
        return root