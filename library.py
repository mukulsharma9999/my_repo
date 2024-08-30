import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
transpose_matrix = matrix.T
print(matrix)
print(transpose_matrix)


tuple_test = [(1,2),(3,4),(5,6)]
sorted_list = sorted(tuple_test,key=lambda x : x[1])
print(sorted_list)