while True:
    try:
        T = int(raw_input())
        for i in xrange(T):
            A = raw_input()
            B = dict()
            for index in A:
                B[index] = B.get(index,0) + 1
            for out in A:
                if B[out] == 1:
                    print out
                    break
    except:
        break