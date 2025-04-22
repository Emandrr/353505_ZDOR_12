import numpy as np


class Matrix:
    def __init__(self, rows, columns):
        # Initialize the matrix with the given number of rows and columns
        self._matrix = np.ndarray([rows, columns])
        self._rows = rows
        self._columns = columns

    def generateMatrix(self, a: int, b: int):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            creating a matrix
            """
        self._matrix = np.random.rand(a, b)

    def display(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            displaying the matrix
            """
        print(self._matrix)


class AdvancedMatrix(Matrix):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.generateMatrix(rows, columns)

    def insert_after_min(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            insert after min row
            """
        minimum = np.min(self._matrix)
        min_row_index = np.where(self._matrix == minimum)[0][0]
        first_row = self._matrix[0]
        new_matrix = np.insert(self._matrix, min_row_index + 1, first_row, axis=0)
        print("Исходная матрица:\n", self._matrix, "\nИзмененная матрица\n", new_matrix)

    def calculate_median_self(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of median
            """
        suma = 0
        for tmp in self._matrix[0]:
            suma += tmp
        return suma/self._columns

    def calculate_median_np(self):
        return self._matrix[0].mean()
