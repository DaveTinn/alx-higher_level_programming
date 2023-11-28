#!/usr/bin/python3
digits = 0
while digits <= 89:
    if digits % 10 == 0:
        digits = digits + 1 + digits // 10
    print("{:02d}".format(digits), end='\n' if digits == 89 else ', ')
    digits = digits + 1
