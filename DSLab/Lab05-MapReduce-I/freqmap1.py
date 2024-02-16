import sys
for line in sys.stdin:
    line = line.strip()
    L = [ (word.strip().lower(), 1 ) for word in line.strip().split() ]
    for word, n in L:
        print( '%s\t%d' % (word, 1) )
