# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# """

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # map to keep track of nodes traversed 
        # and returning reference of that node when adding neighbors
        old_n_new = {}
        
        def dfs(node):
            if node in old_n_new :
                return old_n_new[node]  
            
            # Create copy node and add it to the map
            copy = Node(node.val)
            old_n_new[node] = copy
            
            # Adding all neighbors of the node and recursively calling them as well
            for i in node.neighbors :
                copy.neighbors.append(dfs(i))
            return copy
                
        return dfs(node) if node else None
        