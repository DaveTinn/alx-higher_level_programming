#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    num_of_args = len(argv)
    if num_of_args != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
    }
    if argv[2] in operators:
        num_1 = int(argv[1])
        num_2 = int(argv[3])
        operators = operators[argv[2]]
        result = operators(num_1, num_2)
        print("{:d} {:s} {:d} = {:d}".format(num_1, argv[2], num_2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
