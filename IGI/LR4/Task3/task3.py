from Task3 import graph
import input_self


def menu_task3():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        menu of task 3
        """
    x = input_self.user_input("Введите х (-1,1) ", float, -0.999999, 0.999999)
    eps = input_self.user_input("Введите эпсилон (0,1) ", float, 0, 1)
    graph.generate_table(x, eps)
    graph.generate_add_data(x, eps)
    graph.generate_graphic(x, eps)
