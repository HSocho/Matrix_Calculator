from matrix_calculator import * 
import pytest

matrix0 = [[0,0],[0,0]]
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
matrix3 = [[5, 6], [5, 6]]
matrix4 = [[5],[2]]

def test_matrix_add():
    assert matrix_add(matrix1, matrix2) == [[6, 8], [10, 12]]
    with pytest.raises(ValueError, match="Matrices are not of the same type"):
        matrix_add(matrix1,matrix4)

def test_matrix_multiply():
    assert matrix_multiply(matrix1, matrix2) == [[19, 22], [43, 50]]
    assert matrix_multiply(matrix0, matrix2) == [[0, 0], [0, 0]]
    with pytest.raises(ValueError, match="Wrong type of matrices"):
        matrix_multiply(matrix4, matrix1)

def test_matrix_determinant():
    assert matrix_determinant(matrix1) == -2
    assert matrix_determinant(matrix3) == 0
    with pytest.raises(ValueError, match="Matrix is not square"):
        matrix_determinant(matrix4)

def test_matrix_transpose():
    assert matrix_transpose(matrix1) == [[1, 3], [2, 4]]

def test_matrix_inverse():
    assert matrix_inverse(matrix1) == [[-2, 1], [1.5, -0.5]] 
    with pytest.raises(ValueError, match="Matrix is not square"):
        matrix_inverse(matrix4)
    with pytest.raises(ValueError, match="Matrix is not invertible"):
        matrix_inverse(matrix3)

def test_lu_decomposition():
    L, U = lu_decomposition(matrix1)
    correct_L = [[1, 0], [3, 1]]
    correct_U = [[1, 2], [0, -2]]
    assert L == correct_L
    assert U == correct_U
    with pytest.raises(ValueError, match="Matrix is singular or decomposition requires pivoting"):
        lu_decomposition(matrix3)
    with pytest.raises(ValueError, match="Matrix is not square"):
        lu_decomposition(matrix4)