# Author: Robin Lin
# Matrix Math Library

def dimension(A):
        m = len(A)
        n = len(A[0])
        # return 2-tuple
        return (m,n)

def matrix_multiply(A,B):
        #A,B are nested lists
        #Example: [[1,0,0],[0,1,0],[0,0,1]] is the identity matrix
        # 1 0 0
        # 0 1 0
        # 0 0 1
        dim_A = dimension(A)
        dim_B = dimension(B)
        output_dim = [dim_A[0],dim_B[1]]
        matrix_out = [0] * output_dim[0]
        accum = 0
        for i in range(output_dim[0]):
                matrix_out[i] = [0] * output_dim[1]
        for i in range(0,dim_A[0]):
                for j in range(0,dim_B[1]):
                        for index in range(0,dim_A[1]):
                                accum = accum + A[i][index]*B[index][j]
                        matrix_out[i][j] = accum
                        #reset accum
                        accum = 0
        return matrix_out

def determinant_three(A):
        det = A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[2][0]*A[1][1])
        return det

def invertibility(A):
        # invertibility determines if matrix is singular or non-singular
        # Easiest way to determine is by computing the determinant
        if determinant_three(A) != 0:
                return 1
        else:
                return -1

def dot_product(A,B):
        #A, B are n-by-1 matrices, or simply, vectors in R^n
        dimA = len(A)
        dimB = len(B)
        accum = 0
        if dimA != dimB:
                # error checking
                return -1
        else:
                for i in range(0,dimA):
                        accum = accum + A[i]*B[i]
        return accum

def transpose(A):
        m = len(A)
        n = len(A[0])
        new = [0] * n
        for i in range(n):
                new[i] = [0] * m
        for i in range(0,m):
                for j in range(0,n):
                        new[j][i] = A[i][j]
        return new
