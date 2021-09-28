# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        columns = len(board[0])
        cnt = 0
        path = set()
        
        # Perform DFS from the current cell in all 4 directions until word is found
        def dfs(r,c,i):
            # If value of i becomes equal to length of word this means all characters were found
            if i == len(word):
                return True
            
            # Handling out of bound, different character and already visited cell cases
            if (r<0 or c<0 or r>=rows or c>=columns or board[r][c]!=word[i] or (r,c) in path):
                return False
            
            # If all above cases are False then it indicates current cell has character we are looking for
            path.add((r,c))
            
            # Do DFS from current cell in all 4 directions for next character
            res = (dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1))
            
            # Empty path set for next fresh iteration
            path.remove((r,c))
            
            return res
        
        for i in range(rows):
            for j in range(columns):
                if(dfs(i,j,0)):
                    return True
        return False
            