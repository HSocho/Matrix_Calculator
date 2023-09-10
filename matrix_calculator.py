from fractions import Fraction

def main():
    while True:
        print("MATRIX CALCULATOR")
        print("1. Matrix Addition")
        print("2. Matrix Multiplication")
        print("3. Matrix Determinant")
        print("4. Matrix Transpose")
        print("5. Matrix Inverse")
        print("6. LU Decomposition")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            try:
                matrix1 = get_matrix_choice(" first")
                matrix2 = get_matrix_choice(" second", "add", len(matrix1), len(matrix1[0]))
                result = matrix_add(matrix1, matrix2)
                get_ouput_choice(result)
            except ValueError as e:
                print(e)
        elif choice == 2:
            try:
                matrix1 = get_matrix_choice(" first")
                matrix2 = get_matrix_choice(" second", "multy",None, len(matrix1[0]))
                result = matrix_multiply(matrix1, matrix2)
                get_ouput_choice(result)
            except ValueError as e:
                print(e)
        elif choice == 3:
            try:
                matrix = get_matrix_choice("", "square")
                determinant = matrix_determinant(matrix)
                print("Determinant:", determinant)
            except ValueError as e:
                print(e)
        elif choice == 4:
            matrix = get_matrix_choice("")
            transpose = matrix_transpose(matrix)
            get_ouput_choice(transpose)
        elif choice == 5:
            try:
                matrix = get_matrix_choice("", "square")
                inverse = matrix_inverse(matrix)
                get_ouput_choice(inverse)
            except ValueError as e:
                print(e)
        elif choice == 6:
            try:
                matrix = get_matrix_choice("", "square")
                print("Partial LU decomposition:")
                L, U = lu_decomposition(matrix)
                get_ouput_choice(L)
                get_ouput_choice(U)
            except ValueError as e:
                print(e)
        elif choice == 7:
            print("Exiting the Matrix Calculator")
            break
        else:
            print("Invalid choice. Please enter a valid option")

def get_matrix_choice(prompt = None, operation= None, rows = None, cols = None):
    while True:
        print(f"Choose how you want to input the{prompt} matrix:")
        print("1. Manually")
        print("2. From a file")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Enter/Paste your matrix. Enter an empty line to finish.")
            matrix = []
            while True:
                line = input()
                if not line:
                    break
                try:
                    row = [float(element) for element in line.strip().split()]
                except ValueError:
                    print("Invalid characters. Please try again")
                    continue
                matrix.append(row)
                if len(row) != len(matrix[0]):
                    matrix = []
                    print("Invalid row length. Please try again:")
                else:
                    if operation == "add":  
                        if len(row) != cols:
                            matrix = []
                            raise ValueError("Matrices are not of the same type")
                        if len(matrix) > rows:
                            matrix = []
                            raise ValueError("Matrices are not of the same type")
                    if operation == "multy":
                        if len(matrix) > cols:
                            matrix = []
                            raise ValueError ("Wrong type of matrices")
                    if operation == "square":
                        if len(matrix) > len(matrix[0]):
                            matrix = []
                            raise ValueError ("Matrix is not square")
            return matrix
        elif choice == 2:
            filename = input("Enter the file path: ")
            matrix = read_matrix_from_file(filename)
            if operation == "add":
                if len(matrix[0]) != cols:
                        raise ValueError ("Matrices are not of the same type")
                if len(matrix) > rows:
                    raise ValueError ("Matrices are not of the same type")
            if operation == "multy":
                if len(matrix) > cols:
                    raise ValueError ("Wrong type of matrices")
            if operation == "square":
                if len(matrix) > len(matrix[0]):
                    raise ValueError ("Matrix is not square")
            return matrix
        else:
            print("Invalid choice")

def is_valid_matrix(matrix):
    if not matrix:
        return False 

    num_columns = len(matrix[0])
    for row in matrix:
        if len(row) != num_columns:
            return False  

    return True

def read_matrix_from_file(filename):
    while True:
        try:
            matrix = []
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        row = [float(element) for element in line.replace("[", "").replace("]", "").strip().split()]
                        matrix.append(row)
                    except ValueError:
                        print("Invalid characters. Please try again")
                        filename = input("Enter the file path: ")
            if is_valid_matrix(matrix):
                print("Input successful")
                return matrix
            else:
                print(f"Invalid matrix in the file '{filename}'. Please provide a valid matrix file.")
                filename = input("Enter the file path: ")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please provide a valid path")
            filename = input("Enter the file path: ")

def get_ouput_choice(matrix):
    while True:
        print(f"Choose how you want to ouput the result:")
        print("1. Print")
        print("2. Into a file")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print_matrix(matrix)
            return
        elif choice == 2:
            filename = input("Enter the file path: ")
            save_matrix_to_file(matrix, filename)
            return
        else:
            print("Invalid choice")

def save_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            formatted_row = "["+ " ".join(str(float(Fraction(element).limit_denominator())) for element in row) + "]"
            file.write(formatted_row)
            file.write("\n")

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Wrong type of matrices")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def matrix_add(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices are not of the same type")
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def matrix_determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix is not square")
    if len(matrix) == 2:
        return float(Fraction(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]).limit_denominator())
    determinant = 0
    for i in range(len(matrix)):
        submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        determinant += matrix[0][i] * matrix_determinant(submatrix) * (-1)**i
    return float((Fraction(determinant).limit_denominator()))

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix is not square")
    n = len(matrix)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    calculation_matrix = [row + identity[i] for i, row in enumerate(matrix)]
    
    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(calculation_matrix[j][i]) > abs(calculation_matrix[pivot_row][i]):
                pivot_row = j
        
        calculation_matrix[i], calculation_matrix[pivot_row] = calculation_matrix[pivot_row], calculation_matrix[i]
        
        pivot_element = calculation_matrix[i][i]
        if pivot_element == 0:
            raise ValueError("Matrix is not invertible")
        
        for j in range(i, 2 * n):
            calculation_matrix[i][j] /= pivot_element
        
        for k in range(n):
            if k != i:
                factor = calculation_matrix[k][i]
                for j in range(i, 2 * n):
                    calculation_matrix[k][j] -= factor * calculation_matrix[i][j]
    
    inverse = [row[n:] for row in calculation_matrix]
    inverse = [[float(Fraction(num).limit_denominator()) for num in row] for row in inverse]
    return inverse

def lu_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix is not square")
    for i in range(n):
        L[i][i] = 1.0
        
        for j in range(i, n):
            U[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
        if U[i][i] == 0:
            raise ValueError("Matrix is singular or decomposition requires pivoting")
        
        for j in range(i + 1, n):
            L[j][i] = (matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    
    return L, U

def print_matrix(matrix):
    print("Result:")
    for row in matrix:
        formatted_row = " ".join(str(float(Fraction(element).limit_denominator())) for element in row)
        print(f"[{formatted_row}]")


if __name__ == "__main__":
    main()