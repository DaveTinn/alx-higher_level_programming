#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_Digit = number % 10
else:
    last_Digit = ((number * -1) % 10) * -1
print_msg = 'Last digit of {} is {} '.format(number, last_Digit)
if last_Digit > 5:
    print(print_msg, 'and is greater than 5')
elif last_Digit == 0:
    print(print_msg, 'and is 0')
elif last_Digit < 6:
    print(print_msg, 'and is less than 6 and not 0')
