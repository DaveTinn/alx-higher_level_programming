#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_Digit = number % 10
if last_Digit > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, last_Digit))
elif last_Digit == 0:
    print('Last digit of {} is {} and is 0'.format(number, last_Digit))
elif last_Digit < 6:
    last_Digit != 0
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, last_Digit))
