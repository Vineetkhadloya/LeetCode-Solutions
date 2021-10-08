# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

class Codec:

    def serialize(self, root):
        res = []
        
        # Perform DFS on Tree from root
        def dfs(root):
            # if current node is null it indicates child of leaf node and denote it by "N"
            if not root:
                res.append("N")
                return

            # Add root node to result and then perform dfs on left and right child
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res = ",".join(res)
        print(res)
        return res
        

    def deserialize(self, data):
        data = data.split(",")
        self.i = 0
        
        # Recursively call dfs from start of array and keep moving pointer forrward
        def dfs():
            if(data[self.i] == "N"):
                self.i += 1
                return None
            
            # Create node with data at current pointer
            node = TreeNode(int(data[self.i]))
            # Increment pointer by 1 and create left and right sub - trees
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()