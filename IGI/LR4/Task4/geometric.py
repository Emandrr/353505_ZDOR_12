from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class FigureColor:
    def __init__(self, val):
        self._color = val

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


class IsoTriangle(GeometricFigure):
    _figure_name = "Треугольник"

    def __init__(self, side, color, height) -> None:
        self._side = side
        self._color = FigureColor(color)
        self._height = height

    @property
    def figure_name(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            getter of figure name
            """
        return self._figure_name

    @figure_name.setter
    def figure_name(self, value):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            setter of figure name
            """
        self._figure_name = value

    def calculate_area(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of figure area
            """
        return self._side*self._height/2

    def __str__(self):
        return "{} со стороной {} единиц, цвет: {}, площадь: {:.2f} кв.ед.".format(
            self.figure_name, self._side, self._color.color, self.calculate_area()
        )

    def draw(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            drawing of figure
            """
        base = self._side
        height = self._height
        x = [-base / 2, base / 2, 0]
        y = [0, 0, height]

        if self._color.color == "красный":
            plt.fill(x, y, "red")
        elif self._color.color == "зеленый":
            plt.fill(x, y, "green")
        elif self._color.color == "синий":
            plt.fill(x, y, "blue")
        elif self._color.color == "черный":
            plt.fill(x, y, "black")
        elif self._color.color == "желтый":
            plt.fill(x, y, "yellow")

        plt.axis("equal")
        plt.xlim(min(x) - 1, max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)
        plt.text(0, -height / 2 - 2, self.figure_name, ha="center")  # Подпись под треугольником
        plt.savefig("figure.png")

        plt.show()
