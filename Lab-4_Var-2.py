'''Scriti programul care calculează media aritmetică a elementelor unei matrice'''

import numpy as np


def define_matrix():
    matrix_columns = int(input('Kindly define a number of matrix columns: '))
    matrix_rows = int(input('Kindly define a number of matrix rows: '))

    matrix = []

    if (matrix_columns > 1 and matrix_rows > 1):
        for n in range(0, matrix_rows, 1):
            matrix_row = []
            for i in range(0, matrix_columns, 1):
                user_input = float(input(f'Define the element {n+1}:{i+1}: '))
                matrix_row.append(user_input)
            matrix.append(matrix_row)
    else:
        print("Invalid arguments, restart the program to define a matrix again")

    print(f'Defined matrix: {matrix}')
    return matrix


def find_matrix_mean(matrix):
    x = np.array(matrix)
    return x.mean()


print(find_matrix_mean(define_matrix()))
