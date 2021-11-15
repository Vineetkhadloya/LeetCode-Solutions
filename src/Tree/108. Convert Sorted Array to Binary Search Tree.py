# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(l,r):
            
            if l > r :
                return None
            
            m = (l + r)//2
            root = TreeNode(nums[m])
            root.left = BST(l,m-1)
            root.right = BST(m+1,r)
            
            return root
        
        return BST(0,len(nums)-1)