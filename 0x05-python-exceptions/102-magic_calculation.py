#!/usr/bin/python3
def magic_calculation(a, b):
    magic_result = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception("Not in range")
            magic_result += a ** b / idx
        except Exception:
            magic_result = b + a
            break
    return magic_result
