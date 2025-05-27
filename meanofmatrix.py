'''
Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

Example:
Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'
Output:
[4.0, 5.0, 6.0]
Reasoning:
Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3].
'''
import numpy as np

def calculate_matrix_mean(matrix, mode):
    try:
        np_matrix = np.array(matrix, dtype=float)
    except ValueError:
        raise ValueError('input matrix must have consistent row lwngth and numeric values to be converted to a numpy array')
    
    if np_matrix.size == 0:
        if mode == 'row' or mode == 'column':
            return[]
        else:
            raise ValueError('mode must be row or column')
        
    num_rows, num_cols = np_matrix.shape
    if mode == 'row':
        if num_cols == 0:
            return[0.0] * num_rows
        means = np_matrix.mean(axis=1)
    elif mode == 'column':
        if num_rows == 0:
            return [0.0] * num_cols
        means = np_matrix.mean(axis=0)
    else: 
        raise ValueError("mode must be row or column")
    
    return means.tolist()