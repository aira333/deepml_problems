'''
Write a Python function that calculates the 
eigenvalues of a 2x2 matrix. 
The function should return a list containing the
eigenvalues, sort values from highest to lowest.

Example:
Input:
matrix = [[2, 1], [1, 2]]
Output:
[3.0, 1.0]
Reasoning:
The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, 
which for a 2x2 matrix is 
(lambda)^2 - trace(A)lambda + det(A) = 0

trace is the sum of diagonal elements in matrix

'''

import math

def calculate_eigenvalues_(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    # calculating trace (which is just the sum of diagonals of the matrix)
    
    trace_A = a + d
    
    # calculating the determinant
    
    det_A = (a * d) - (b * c)
    
    # caclulating the discriminant ( b**2 - 4*a*c)
    
    discriminant = (trace_A**2) - (4 * det_A)
    
    # handle cases where eigen values maybe complex (discriminat < 0)
    if discriminant < 0:
        raise ValueError("Matrix has complex eigenvalues")
    
    # calculate the two eigenvalues using the quadratic formaula
    
    lambda1 = (trace_A + math.sqrt(discriminant)) / 2
    lambda2 = (trace_A - math.sqrt(discriminant)) / 2
    
    # put the eigenvalues into a list
    
    eigenvalues = [lambda1, lambda2]
    
    #sort the eigenvalues from the highest to lowest
    
    eigenvalues.sort(reverse=True) #descending order
    
    return eigenvalues
    
    
    
    
    
    
    
    