import sys

args = sys.argv[1:]
while '' in args:
    args.remove('')
if len(args) > 0:
    print(' '.join(args)[::-1].swapcase())
