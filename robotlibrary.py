from math import *

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


def rotation(axis,angle):
        # encoding scheme
        # 1 - x, 2- y, 3 - z
        r = [[0,0,0],[0,0,0],[0,0,0]]
        if axis == 1:
                r = [[1,0,0],[0,cos(angle),-sin(angle)],[0,sin(angle),cos(angle)]]
        elif axis == 2:
                r = [[cos(angle),0,sin(angle)],[0,1,0],[-sin(angle),0,cos(angle)]]
        elif axis == 3:
                r = [[cos(angle),-sin(angle),0],[sin(angle),cos(angle),0],[0,0,1]]

        return r

def nonhomo_to_homo_c(pos):
        if len(pos) != 3:
                return -1
        new = pos + [1]
        return new


def shear(theta):
        # shear -> apply tilt to object
        s_x = [[1,cot(theta),0],[0,0,0],[0,0,1]]
        return s_x

def translation(dx,dy,dz):
        trans = [dx,dy,dz]
        return trans

def generate_affine_transform(ul,ur):
        # affine transformation matrix is defined as follows:
        #      ----                    ----
        #      |             |            |
        #      |  upper-left | upper-right|
        #      |             |            |
        #      |-------------|------------|
        #      |             |            |
        #      |             |            |
        #      | 0    0    0 |      1     |
        #      |                          |
        #      ----                    ----

        matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        # build upper-left
        for i in range(0,3):
                for j in range(0,3):
                	matrix[i][j] = ul[i][j]
	#build upper-right
	for i in range(0,3):
		matrix[i][3] = ur[i]
	matrix[3][3] = 1
	return matrix

ul = rotation(1,pi/2)
ur = translation(1,2,3)
print generate_affine_transform(ul,ur)
