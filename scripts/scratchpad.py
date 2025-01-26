from src.ray_tracer import RTMatrix

m1 = RTMatrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

"""
[
[1 2 3]
[4 5 6]
[7 8 9]
]

iterate thru the list
"""
# m1.transpose(inplace=True)
print(m1.data)

print(m1.submatrix(2, 2).data)
print(m1.data)
