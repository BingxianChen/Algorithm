while True:
    try:
        n = raw_input()
        M = list(n)
        m = sorted(n)
        a = 0
        for i in xrange(len(M)):
            if M[i] != m[i]:
                a += 1
        print a
    except:
        break