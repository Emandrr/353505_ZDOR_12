import Input


def string_analyze():
    """
        Developer Pavel Zdor
        date: 10.03.2025
        function is developed for calculating number of amount of upper vowels in string
        supports 2 mods: user and rand input
        :return:
        """
    user_choose = Input.user_input("Enter variant: 0 - random input, 1 - user input  ", int, 0, 1)
    counter = 0
    if user_choose == 1:
        text_to_analyze = Input.user_input("Input string ", str, None, None)
        for i in text_to_analyze:
            if ('A' <= i <= 'Z') and (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Y'):
                counter += 1
    if user_choose == 0:
        text_to_analyze = Input.rand_input("string is  ", str, 1, 25)
        for i in text_to_analyze:
            if ('A' <= i <= 'Z') and (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Y'):
                counter += 1
    print("Amount of upper vowels",counter)
