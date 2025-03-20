import Input


def Task5():
    """
        Developer Pavel Zdor
        date: 11.03.2025
        function is developed for calculating a number of  elements in list between two integers and sum after maximum element
        prints a minimum
        supports 2 mods: user and rand input
        :return:
        """
    counter = 0
    a = user_input_float()
    data_list = check(a)
    while data_list is None:
        a = user_input_float()
        data_list = check(a)
    if data_list is not None:
        print_list(data_list)
        initial_solve(data_list)


def user_input_float():
    a = input("Input all number by space in one line: ")
    return a


def check(a):
    try:
        list_of_str = a.split(' ')
        list_of_number = [float(i) for i in list_of_str if i != '']
        return list_of_number
    except Exception as e:
        print(e)
        return None


def initial_solve(data_list):
    a = Input.user_input("Input left border ", int, 0, len(data_list) - 1)
    b = Input.user_input("Input right border ", int, a, len(data_list) - 1)
    counter = b - a + 1
    sums = 0
    maximum = float('-inf')
    index = 0
    ind = 0
    for i in data_list:
        if maximum < i:
            maximum = i
            ind = index
        index += 1
    index = 0
    for i in data_list:
        if index > ind:
            sums += i
        index += 1
    print("Amount of elements between a and b in list is", counter)
    print("Sum after max element", sums)


def print_list(data_list):
    print("list is", data_list)
