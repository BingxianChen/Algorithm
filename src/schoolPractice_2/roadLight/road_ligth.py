while True:
    try:
        n,l = [int(i) for i in raw_input().split()]
        A = [int(i) for i in raw_input().split()]
        A.sort()
        B = []
        for i in range(0,n-1):
            B.append(A[i + 1] - A[i])
        B.append(2*A[0])
        B.append(2*(l - A[n - 1]))
        print "%.2f"%(float(max(B))/2)

    except:
        break
