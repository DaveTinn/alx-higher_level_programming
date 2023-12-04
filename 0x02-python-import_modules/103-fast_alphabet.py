#!/usr/bin/python3
for alphabets in range(65, 91):
    print("{:c}".format(alphabets), end="") if alphabets else print("\n", end="")
