from Task5 import matrix
import input_self


def menu_task5():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        menu of task 5
        """
    m = input_self.user_input("Введите количество строк матрицы: ", int, 1, 10000)
    n = input_self.user_input("Введите количество столбцов матрицы: ", int, 1, 10000)

    integer_matrix = matrix.AdvancedMatrix(m, n)
    print("Исходная матрица:")
    integer_matrix.display()
    print()
    integer_matrix.insert_after_min()
    print()
    print("Медиана расчитанная вручную:")
    print(integer_matrix.calculate_median_self())
    print()
    print("Медиана расчитанная с помощью numpy:")
    print(integer_matrix.calculate_median_np())