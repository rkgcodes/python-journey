# demonstarte sys.exit

import sys

if len(sys.argv)<2:
    sys.exit("Too few arguments")

elif len(sys.argv)>2:
    sys.exit("Too many arguments")

else:
    print("hello, my name is", sys.argv[1])
    