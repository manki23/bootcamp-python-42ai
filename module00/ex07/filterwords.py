import sys
import string
import re

args = sys.argv[1:]
if len(args) != 2 or not isinstance(args[0], str) or not args[1].isnumeric() or args[0].isnumeric():
    print("ERROR")
else:
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    words = regex.sub('', str(args[0])).split()
    nb = int(args[1])
    result = []
    for elem in words:
        if len(elem) > nb: result.append(elem)
    
    print(result)
