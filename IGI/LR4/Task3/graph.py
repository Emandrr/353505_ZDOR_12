from Task3 import SequenceAnalyzers
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


def generate_table(x, eps):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        creating a table
        """
    analyze = SequenceAnalyzers.SequenceAdvanced(x, eps)
    taylor = (analyze.taylor_series())
    f_x = (analyze.calculate_real())
    table_data = [
        [x, taylor[0], taylor[1], f_x, eps]
    ]
    table_headers = ["x", "Итерации", "F(x)", "Математический F(x)", "Точность"]
    table = tabulate(table_data, headers=table_headers)
    print(table)


def generate_graphic(x, eps):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        creating graphic of function
        """
    sequence = np.arange(x, x+1, eps)
    y = []
    y1 = []
    for x in sequence:
        analyze = SequenceAnalyzers.SequenceAdvanced(x, 0.00001)
        y.append(analyze.taylor_series()[1])
        y1.append(analyze.calculate_real())
    plt.plot(sequence, y, color="blue", label="Ряд")
    plt.plot(sequence, y1, color="red",
             linestyle="--", label="Математический F(x)")
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.legend()
    plt.grid(True)
    plt.title("График разложения функции в ряд")

    plt.savefig("Task3.png")

    plt.show()


def generate_add_data(x, eps):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        creating data and writes to console
        """
    sequence = np.arange(-0.99999, 0.99999, eps)
    seq_analyze = SequenceAnalyzers.SequenceBase(sequence)
    print("Среднее арифметическое:", seq_analyze.calculate_mean)
    print("Медиана:", seq_analyze.calculate_median)
    print("Мода:", seq_analyze.calculate_mode)
    print("Дисперсия:", seq_analyze.calculate_variance)
    print("Стандартное отклонение:", seq_analyze.calculate_standard_deviation)
