import sys

if len(sys.argv[1:]) > 0:
    print(' '.join(sys.argv[1:])[::-1].swapcase())
