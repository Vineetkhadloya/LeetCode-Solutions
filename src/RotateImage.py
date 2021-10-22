# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.


# This can be achived by creating a transpose of the matrix and then reflection of the transposed matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Create Transpose of the Matrix
        for i in range(n):
            for j in range(i,n):
                # Swapping values
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reflect the Transposed Matrix
        for i in range(n):
            for j in range(n//2):
                # Swapping values
                matrix[i][j],matrix[i][-j-1]=matrix[i][-j-1],matrix[i][j]