import Task1
import Task2
import Task3
import Task4
import Task5
import Input


def menu():
    """
        Developer Pavel Zdor
        date: 11.03.2025
        function is developed for choosing one of five provided functions
        :return:
        """
    while True:
        user_chs = Input.user_input("0 - exit from program, 1 - Calculate Taylor series, "
                                    "2 - Find minimum in input and sum, 3 - Analyze string of upper vowels"
                                    " 4 - Analyze predefined text, 5 - analyze float list with borders ", int, 0, 5)
        if user_chs == 0:
            return
        elif user_chs == 1:
            Task1.calc()
        elif user_chs == 2:
            Task2.find_minimum()
        elif user_chs == 3:
            Task3.string_analyze()
        elif user_chs == 4:
            Task4.text_analyze()
        elif user_chs == 5:
            Task5.Task5()
