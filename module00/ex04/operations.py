import sys


def str_is_nb(nb):
    if not nb.isnumeric() and not (nb[0] == "-" and nb[1:].isnumeric()):
        return False
    else:
        return True


def print_usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n\tpython operations.py 10 3")


args = sys.argv[1:]
if len(args) > 2:
    print("InputError: too many arguments\n")
    print_usage()
elif len(args) == 0:
    print_usage()
elif len(args) == 1:
    print("InputError: too few arguments\n")
    print_usage()
elif not str_is_nb(args[0]) or not str_is_nb(args[1]):
    print("InputError: only numbers\n")
    print_usage()
else:
    sum = int(args[0]) + int(args[1])
    diff = int(args[0]) - int(args[1])
    prod = int(args[0]) * int(args[1])
    if float(args[1]) == 0:
        div = "ERROR (div by zero)"
        mod = "ERROR (modulo by zero)"
    else:
        div = int(args[0]) / int(args[1])
        mod = int(args[0]) % int(args[1])
    print("Sum:\t\t{0}".format(sum))
    print("Difference:\t{0}".format(diff))
    print("Product:\t{0}".format(prod))
    print("Quotient:\t{0}".format(div))
    print("Remainder:\t{0}".format(mod))
