'''
Write a Python function that computes the transpose of a given matrix.

Example:
Input:
a = [[1,2,3],[4,5,6]]
Output:
[[1,4],[2,5],[3,6]]
Reasoning:
The transpose of a matrix is obtained by flipping rows and columns.

'''

def transpose_matrix(self, a):
    if not a:
        return []
    
    a_rows = len(a)
    a_cols = len(a[0])
    
    for row in a:
        if len(row) != a_cols:
            return []
        
    b = [[0 for _ in range(a_rows)] for _ in range(a_cols)]
    
    for i in range(a_rows):
        for j in range(a_cols):
            b[j][i] = a[i][j]
            
    return b
        