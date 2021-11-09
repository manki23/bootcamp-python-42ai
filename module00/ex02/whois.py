import sys

if (len(sys.argv[1:]) > 1):
    print("ERROR")
elif len(sys.argv[1:]) == 1:
    nb = sys.argv[1]
    if not nb.isnumeric() and not (nb[0] == "-" and nb[1:].isnumeric()):
        print("ERROR")
    elif int(nb) == 0:
        print("I'm Zero.")
    elif int(nb) % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
