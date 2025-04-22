import input_self
from Task4 import geometric


def menu_task4():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        menu of task 4
        """
    side = input_self.user_input("Введите размер основания: ", float, None, None)
    height = input_self.user_input("Введите размер высоты к основанию: ", float, None, None)
    allowed_colors = ["красный", "зеленый", "синий", "черный", "желтый"]
    color = input_self.user_input("Введите цвет фигуры(красный, зеленый, синий, черный, желтый): ", str, None, None)
    while color.lower() not in allowed_colors:
        print("Недопустимый цвет! Попробуйте снова.")
        color = input_self.user_input("Введите цвет фигуры(красный, зеленый, синий, черный, желтый): ", str, None, None)
    tr = geometric.IsoTriangle(side, color, height)
    print(tr)
    tr.draw()
