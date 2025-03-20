import sys
import Input


def find_minimum():
    """
    Developer Pavel Zdor
    date: 09.03.2025
    function is developed for calculating minimum of integers
    prints a minimum
    supports 2 mods: user and rand input
    :return:
    """
    sum = 0
    x = -1
    min_number = None
    user_choose = Input.user_input("Enter variant: 0 - random input, 1 - user input  ", int, 0, 1)
    if user_choose == 0:
        while x != 0:
            x = Input.rand_input("rand value is", int, -25, 25)
            sum += x
            if min_number is None:
                min_number = x
            elif min_number > x:
                min_number = x
    if user_choose == 1:
        while x != 0:
            x = Input.user_input("input value ", int, -sys.maxsize, sys.maxsize)
            sum += x
            if min_number is None:
                min_number = x
            elif min_number > x:
                min_number = x
    print("min value is", min_number, "sum of input is", sum)
