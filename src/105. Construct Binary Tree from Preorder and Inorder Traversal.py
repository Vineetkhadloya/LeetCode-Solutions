# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# (a) Inorder (Left, Root, Right)
# (b) Preorder (Root, Left, Right)
# (c) Postorder (Left, Right, Root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # return None if list is empty
        if not preorder:
            return None
        
        # First element of preorder list is root node
        root = TreeNode(preorder[0])
        # Find location of root in inorder list which helps in determining left and right subtree
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root