# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        print("preorder = ",preorder)
        
        # If List is empty then return None ==> Leaf Node Child
        if not preorder: return None
        
        root = TreeNode(preorder[0])
        
        print("root = ",root)
        
        # If List length is one then it is leaf Node
        if len(preorder) == 1: return root
        
        # Calculate start of right Sub Tree
        left = 1
        right = len(preorder) - 1

        while left < right:
            print("left,right = ",left,right)
            mid = (left + right) // 2
            if(preorder[mid] < root.val):
                left = mid + 1
            else:
                right = mid

        # Index of left will be starting of right sub tree
        
        # If value of leftmost is less than value of root this indicates there is no right sub tree
        if(preorder[left] < root.val):
            root.left = self.bstFromPreorder(preorder[1:])
        else:
            root.left = self.bstFromPreorder(preorder[1:left])
            root.right = self.bstFromPreorder(preorder[left:])
            
        return root