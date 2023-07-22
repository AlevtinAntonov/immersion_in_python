# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц

class Matrix:
    _rows: int = None
    _cols: int = None
    _matrix: list[list[int, float]] = None

    def __init__(self, matrix: list[list[int, float]] = None) -> None:
        """Matrix initialization
        :param _cols: int - number of columns
        :param _rows: int - number of rows"""
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._matrix = matrix

    def __str__(self):
        """Print matrix"""
        return '\n'.join('\t'.join(map(str, row)) for row in self._matrix)

    def _isinstance(self, other):
        """Check if the objects have the same class"""
        if not isinstance(other, self.__class__):
            raise TypeError("This is not a 'Matrix'")

    def _check_sizes(self, other):
        """Check if matrix have the same sizes"""
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Different size objects")

    def __eq__(self, other):
        """Retun True if matrix equals other"""
        if self is other:
            return True
        self._isinstance(other)
        self._check_sizes(other)

        for i in range(self._rows):
            for j in range(self._cols):
                if self._matrix[i][j] != other._matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        """Sum of two matrixs"""
        self._isinstance(other)
        self._check_sizes(other)
        res_matrix = [[0 for _ in range(self._rows)] for _ in range(self._cols)]
        for i in range(self._rows):
            for j in range(self._cols):
                res_matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return Matrix(res_matrix)

    def __mul__(self, other):
        """Multiplication of two matrixs"""
        self._isinstance(other)
        if self._rows != other._cols or self._cols != other._rows:
            raise ValueError('Number of rows first matrix do not equal the number of columns the other one')
        res_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._rows):
                res_matrix[i][j] = self._matrix[i][j] * other._matrix[j][i]
        return Matrix(res_matrix)


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
    a = Matrix(matrix1)
    b = Matrix(matrix2)
    print(Matrix.__eq__(a, b))
    print()
    print(Matrix.__add__(a, b))
    print()
    print(Matrix.__mul__(a, b))
