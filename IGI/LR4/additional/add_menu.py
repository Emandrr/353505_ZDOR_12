from additional import additionaltask as a
from IPython.display import display


def add_menu():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        menu of additional task
        """
    stats_analyzer = a.MedicineStats('Medicine_Details.csv')

    print("\nСтатистика по производителям:")
    display(stats_analyzer.get_manufacturer_stats())

    print("\nАнализ отзывов:")
    review_stats = stats_analyzer.get_review_stats()
    display(review_stats['best'])
    display(review_stats['worst'])
    print(f"Соотношение лучших и худших отзывов: {review_stats['ratio']:.2f}")

    print("\nСравнение побочных эффектов:")
    side_effects = stats_analyzer.compare_side_effects()
    display(side_effects['max_side'])
    display(side_effects['min_side'])
    print(f"Максимальное количество побочных эффектов больше минимального в {side_effects['ratio']:.2f} раз")