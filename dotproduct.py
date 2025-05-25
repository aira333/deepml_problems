'''
Write a Python function that computes the dot product of a matrix and a vector. 
The function should return a list representing the resulting vector if the operation is valid, 
or -1 if the matrix and vector dimensions are incompatible.
A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns 
in the matrix equals the length of the vector. 
For example, an n x m matrix requires a vector of length m.

'''

def dot_product_matrix_vector(matrix, vector):
    if not matrix:
        return -1
    
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    
    vector_length = len(vector)
    
    if matrix_cols != vector_length:
        return -1
    
    result_vector = [0] * matrix_rows
    
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            result_vector[i] += matrix[i][j] * vector[j]
    return result_vector