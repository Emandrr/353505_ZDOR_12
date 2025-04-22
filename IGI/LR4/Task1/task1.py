import input_self
from Task1 import work_with_file
from Task1 import classes_task1


def menu_task1():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        function of menu of task 1
        """
    list_of_countries_with_cities = []
    list_of_cities = []
    while True:
        print("Меню")
        print("1. Добавить страну и город")
        print("2. Вывести список стран и городов к нему")
        print("3. Отсортировать список по названию города")
        print("4. Вывести информацию о городе введенном с клавиатуры")
        print("5. Сохранить данные в файл CSV")
        print("6. Загрузить данные из файла CSV")
        print("7. Сохранить данные в файл pickle")
        print("8. Загрузить данные из файла pickle")
        print("0. Выход")

        choice = input_self.user_input("Выберите пункт меню: ", int, 0, 10)

        if choice == 1:
            key = input("Введите страну ")
            key = input_self.check_string(key)
            syn = input("Введите ее город ")
            syn = input_self.check_string(syn)
            country = classes_task1.Country(key, syn)
            list_of_countries_with_cities.append(country)
        elif choice == 2:
            for syn in list_of_countries_with_cities:
                syn.get_info()
        elif choice == 3:
            classes_task1.Country.sort_by_val(list_of_countries_with_cities)
        elif choice == 4:
            key = input("Введите город ")
            key = input_self.check_string(key)
            print("Все страны с таким городом ")
            for syno in list_of_countries_with_cities:
                if syno.name_city == key:
                    print(syno.name_country)
        elif choice == 5:
            work_with_file.write_to_csv(list_of_countries_with_cities)
        elif choice == 6:
            list_of_countries_with_cities = work_with_file.load_from_csv()
        elif choice == 7:
            work_with_file.write_to_pickle(list_of_countries_with_cities)
        elif choice == 8:
            list_of_countries_with_cities = work_with_file.load_from_pickle()
        elif choice == 0:
            return
