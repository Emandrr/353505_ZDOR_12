class City:
    """
        Developer Pavel Zdor
        date: 20.04.2025
        base class implementing logic of city
        :return:
        """
    def __init__(self, name):
        self._name_city = name

    @property
    def name_city(self):
        return self._name_city

    @name_city.setter
    def name_city(self, value):
        self._name_city = value


class Country(City):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        base class implementing logic of country
        :return:
        """
    def __init__(self, name_country, name_city,):
        super().__init__(name_city)
        self._name_country = name_country

    @property
    def name_country(self):
        return self._name_country

    @name_country.setter
    def name_country(self, value):
        self._name_country = value

    def get_info(self):
        print("Страна", self._name_country, "город", self.name_city)

    @staticmethod
    def sort_by_val(list_of_countries):
        list_of_countries.sort(key=lambda x: x.name_country)
