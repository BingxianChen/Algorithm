while True:
    try:
        n = int(raw_input().strip())
        min_x = None
        min_y = None
        max_x = None
        max_y = None
        for i in range(0,n):
            x,y = [int(k) for k in raw_input().split()]
            if i == 0:
                min_x = x
                min_y = y
                max_x = x
                max_y = y
                continue
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y

        L = max(max_x - min_x,max_y-min_y)
        print L**2
    except:
        break