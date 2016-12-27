import math
try:
    while 1:
        inputs = raw_input().split()
        oldAvg = int(inputs[1])
        rate = float(inputs[2])
        year = int(inputs[3])
        avgAge = 0
        for _ in range(year):
            avgAge = oldAvg*(1-rate) + 21*rate
            oldAvg = avgAge+1
        print int(math.ceil(avgAge))
except:
    pass