#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [[0] * len(row) for row in matrix]
    for s in range(len(matrix)):
        for k in range(len(matrix[s])):
            res[s][k] = matrix[s][k] ** 2
    return res
