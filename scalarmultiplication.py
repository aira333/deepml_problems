'''
Write a Python function that multiplies a matrix by a scalar and returns the result.

Example:
Input:
matrix = [[1, 2], [3, 4]], scalar = 2
Output:
[[2, 4], [6, 8]]
Reasoning:
Each element of the matrix is multiplied by the scalar.
'''

def scalar_multiplication_of_matrix(matrix, scalar):
    if not matrix:
        return []
    
    num_row = len(matrix)
    num_col = len(matrix[0])
    
    result_matrix = [[0 for _ in range(num_col)] for _ in range(num_row)]
    
    for r in range(num_row):
        for c in range(num_col):
            result_matrix[r][c] = matrix[r][c] * scalar
            
    return result_matrix