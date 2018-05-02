import sys
import numpy.linalg as linalg


def solve_matrix(A, b):
    """ This will call the built in matrix solving utility in numpy and solve
    the matrix equation A.x=b for x.

    inputs
    - A: The matrix generated in a separate function with coefficients of
    temperature at each node
    - b: The array of constants generated by a separate function

    outputs
    - temperature_array: The value of temperatures at each node at a given time
    """

    temperature_array = linalg.solve(A, b)

    return temperature_array
