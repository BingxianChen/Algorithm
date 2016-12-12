while True:
    try:
        n,r,Avg= [int(i) for i in raw_input().split()]
        A = dict()
        count = 0
        Min = n * Avg
        for i in range(0,n):
            ai,bi = [int(i) for i in raw_input().split()]
            count += ai
            A[bi] = A.get(bi,0) + (r - ai)
        B = sorted(A.items(),key = lambda x:x[0])
        t = 0
        if count >= Min:
            print 0
            continue
        for index in B:
            if count + index[1] < Min:
                count += index[1]
                t += index[0] * index[1]
            else:
                t += (Min - count) * index[0]
                print t
                break
    except:
        break