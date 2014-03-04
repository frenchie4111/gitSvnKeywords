import sys

for l in sys.stdin.readlines():
    print("Line: " + l)
    if( l == '\0' ):
        break