from src.ray_tracer import RTMatrix

m1 = RTMatrix(matrix=[[1, 2, 3, 4], [3, 4, 18, 21], [1, 2, 22, 12], [32, 4, -2, 2]])

"""
[
[1 2 3]
[4 5 6]
[7 8 9]
]

iterate thru the list
"""
# m1.transpose(inplace=True)
# print(m1.data)

# print(m1.submatrix(2, 2).data)
# print(m1.data)

# inverse of identity matrix is the identity matrix
# i1 = RTMatrix.identity()
# print(m1.data)
# print(m1.inverse().data)

# # matrix times its inverse is identity matrix
# print((m1 * m1.inverse()) == i1)

# # inverse of transpose is the same as transpose of inverse
# # At^-1 == A^-1t
# print(m1.inverse().transpose() == m1.transpose().inverse())

# c1 = CustomTuple(1, 2, 3, 4)

# print(i1 * c1)

# i1[0][1] = 5

# print(i1 * c1)


import math

print(math.sin()))
