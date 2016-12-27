while True:
    try:
        n = int(raw_input())
        A = [int(i) for i in raw_input().split()]
        A_pre = max([A[i + 1] - A[i] for i in xrange(0,len(A) - 1)])
        aft = [A[i + 1] - A[i - 1] for i in xrange(1,len(A) - 1)]
        if A_pre > min(aft):
            print A_pre
        else:
            print min(aft)
    except:
        break