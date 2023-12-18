#!/usr/bin/python3
def safe_print_division(a, b):
    result_of_div = 0
    try:
        result_of_div = a / b
    except ZeroDivisionError:
        result_of_div = None
    finally:
        print("Inside result: {}".format(result_of_div))
        return result_of_div
