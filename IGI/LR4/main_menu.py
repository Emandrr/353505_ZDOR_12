from Task1 import task1
from Task2 import task2
from Task3 import task3
from Task4 import task4
from Task5 import task5
import input_self
from additional import add_menu


def menu():
    """
        Developer Pavel Zdor
        date: 121.04.2025
        function is developed for choosing one of six provided functions
        """
    while True:
        user_chs = input_self.user_input("0 - exit from program, 1 - Работа со списком стран и городов, "
                                         "2 - Анализ файла, 3 - Функция и ряд Тейлора"
                                         " 4 - Равнобедренный треугольник и его отрисовка"
                                         ", 5 - анализ и работата с матрицей  "
                                         "6 - дополнительное задание", int, 0, 6)
        if user_chs == 0:
            return
        elif user_chs == 1:
            task1.menu_task1()
        elif user_chs == 2:
            task2.menu_task2()
        elif user_chs == 3:
            task3.menu_task3()
        elif user_chs == 4:
            task4.menu_task4()
        elif user_chs == 5:
            task5.menu_task5()
        elif user_chs == 6:
            add_menu.add_menu()



