while True:
    try:
        n,t,c = map(int,raw_input().strip().split())
        crim = map(int,raw_input().strip().split())
        count = 0
        res = sum(crim[0:c])
        if res <= t:
            count += 1
        for i in range(1,n - c + 1):
            res += crim[i + c - 1] - crim[i - 1]
            if res <= t:
                count += 1
        print count
    except:
        break