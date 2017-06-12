while True:
    try:
        line1 = int(raw_input())
        x = [int (i) for i in raw_input().strip().split()]
        y = [int (i) for i in raw_input().strip().split()]
        gx,gy = [int (i) for i in raw_input().strip().split()]
        w,t = [int (i) for i in raw_input().strip().split()]

        C = []
        for i in xrange(line1):
            dx = abs(gx - x[line1 - 1])
            dy = abs(gy - y[line1 - 1])
            _dx = abs(x[line1 - 1])
            _dy = abs(y[line1 - 1])
            C.append(w*(_dx + _dy) + t*(dx + dy))
        C.append(w*(abs(gx) + abs(gy)))

        print min(C)

    except:
        break