import csv
import pickle
from Task1 import classes_task1
import os


def load_from_csv():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        function of loading from csv
        """
    synonyms = []
    with open("synonym.csv", "r") as file:
        _reader = csv.reader(file)
        if os.path.getsize("synonym.csv") != 0:
            next(_reader)
            for row in _reader:
                syn = classes_task1.Country(row[0], row[1])
                synonyms.append(syn)
    return synonyms


def write_to_csv(list_of_countries_with_cities):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        function of writing to csv
        """
    with open("synonym.csv", "w", newline="") as file:
        _writer = csv.writer(file)
        _writer.writerow(["Страна", "Город"])
        for synonym in list_of_countries_with_cities:
            _writer.writerow([synonym.name_country, synonym.name_city])
    print("Данные успешно сохранены в csv")


def load_from_pickle():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        function of loading from pickle
        """
    with open("synonyms.pickle", "rb") as file:
        synonyms = pickle.load(file)
    return synonyms


def write_to_pickle(list_of_countries_with_cities):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        function of writing to pickle
        """
    with open("synonyms.pickle", "wb") as file:
        pickle.dump(list_of_countries_with_cities, file)
    print("Данные успешно сохранены в pickle")