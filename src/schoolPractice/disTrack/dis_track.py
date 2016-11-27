# coding=utf8
import sys
def dist(x1,y1,x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

while True:
    try:
        line = [float(i) for i in sys.stdin.readline().strip(" ").split()]
        R = line[0]
        x = line[7]
        y = line[8]
        count = 0
        for i in range(1,6,2):
            if dist(x,y,line[i],line[i + 1]) <= R:
                count += 1
        print "{0}x".format(count)

    except:
        break