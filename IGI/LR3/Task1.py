import math
import Input
from tabulate import tabulate


def calc():
    """
     Developer Pavel Zdor
     date: 08.03.2025
     function is developed for calculating Taylor Series for logarithm((1+x)/(1-x))
     prints a table with final result in form: "x", "n", "F(x)", "Math F(x)", "eps"
     supports 2 mods: user and rand input
    :return:
     """
    user_choose = Input.user_input("Enter variant: 0 - random input, 1 - user input  ", int, 0, 1)
    if user_choose == 1:
        eps = Input.user_input("Enter eps (0,1  )  ", float, 0, 1)
        x = Input.user_input("Enter x (1.00001,2) ", float, 1.00001, 2)
        math_f = math.log((x + 1) / (x - 1))
        iterations = 500
        n = 0
        res = 0
        while n < iterations and abs(res - math_f) > eps:
            res += 2 * (1 / ((2 * n + 1) * pow(x, 2 * n + 1)))
            n += 1
        table_data = [
            [x, n, res, math_f, eps]
        ]
        table_headers = ["x", "n", "F(x)", "Math F(x)", "eps"]
        table = tabulate(table_data, headers=table_headers)
        print(table)
    if user_choose == 0:
        eps = Input.rand_input("eps is ", float, 0.0, 1.0)
        x = Input.rand_input("x is", float, 1.00000000001, 1.999999999999999)
        math_f = math.log((x + 1) / (x - 1))
        iterations = 500
        n = 0
        res = 0
        while n < iterations and abs(res - math_f) > eps:
            res += 2 * (1 / ((2 * n + 1) * pow(x, 2 * n + 1)))
            n += 1
        table_data = [
            [x, n, res, math_f, eps]
        ]
        table_headers = ["x", "n", "F(x)", "Math F(x)", "eps"]
        table = tabulate(table_data, headers=table_headers)
        print(table)
