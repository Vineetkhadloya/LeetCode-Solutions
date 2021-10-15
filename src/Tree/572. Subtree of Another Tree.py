#Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot 
# and false otherwise.

#A subtree of a binary tree tree is a tree that consists of a node in tree 
# and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # if node with value same as root of subRoot Tree is found
        # isSameTree function helps in checking if both trees are same
        def isSameTree(a,b):
            if not a and not b:
                return True
            
            if (not a or not b) or (a.val!=b.val):
                return False
            
            return (isSameTree(a.left,b.left) and isSameTree(a.right,b.right))
        
        # Initialize a deque and append root to it
        rQ = collections.deque()    
        rQ.append(root)
        
        # Doing Lateral Traversal on main tree and calling isSubTree function if
        # value of node is equal to root of subRoot tree
        while rQ:
            rQLen = len(rQ)
            
            for i in range(rQLen):
                n = rQ.popleft()
                if n:
                    if n.val == subRoot.val:
                        if(isSameTree(n,subRoot)):
                            return True
                    rQ.append(n.left)
                    rQ.append(n.right)
        
        
        return False
            