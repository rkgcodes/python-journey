# demonstrate a t-rex function from pip package
import cowsay
import sys

if len(sys.argv)==2:
    cowsay.trex("hello," + sys.argv[1])
    
    