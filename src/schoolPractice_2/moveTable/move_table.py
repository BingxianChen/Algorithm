while True:
    try:
        r, x, y, x1, y1 = [int(i) for i in raw_input().split()]
        dis = ((x - x1)**2 + (y - y1)**2)**0.5
        print int(dis/2/r)
    except:
        break