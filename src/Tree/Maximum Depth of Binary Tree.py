#Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #print(root)
        
        stack = []
        depth = 0
        
        # Add Tree to stack
        if root is not None:
            stack.append((1,root))
        
        while stack!=[]:
            # Get the last node in the stack
            current_depth, root = stack.pop()
            # If node is not none then add it's childern to the stack
            if root is not None:
                # If depth of current node is greater than previosuly encountered nodes 
                # then depth is updated
                depth = max(depth,current_depth)
                # Adding left child to stack
                stack.append((current_depth+1,root.left))
                # Adding right child to stack
                stack.append((current_depth+1,root.right))
        
        return depth