import random
import string


def user_input(data, data_type, min_value, max_value):
    """
        Developer Pavel Zdor
        date: 11.03.2025
        function is developed for analyzing user input for its acceptance
        :return:
        """
    while True:
        try:
            checked_value = data_type(input(data))
            if max_value is not None and max_value < abs(checked_value):
                raise ValueError(f"Value has to be less than or equal {max_value}")
            if min_value is not None and min_value > abs(checked_value):
                raise ValueError(f"Value has to be more than or equal {min_value}")
            return checked_value
        except ValueError as error:
            print(f"Error: {error}. Please enter a valid value.")


def rand_input(data, data_type, min_value, max_value):
    """
        Developer Pavel Zdor
        date: 11.03.2025
        function is developed for generating random element of provided data_type
        :return:
        """
    if min_value is None:
        min_value = float('-inf')
    if max_value is None:
        max_value = float('inf')

    if data_type == str:
        if min_value is None:
            min_value = 1
        if max_value is None:
            max_value = 10

        checked_value = ''.join(
            random.choices(string.ascii_letters + string.digits, k=random.randint(min_value, max_value)))
        print(data, checked_value)
        return checked_value
    if data_type == int:
        checked_value = random.randint(min_value, max_value)
    elif data_type == float:
        checked_value = random.uniform(min_value, max_value)
    else:
        raise ValueError("Unsupported data type. Supported types are int, float")
    print(data, checked_value)
    return checked_value
