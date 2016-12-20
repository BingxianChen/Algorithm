while True:
    try:
        n,m,x,y,t=map(int,raw_input().split())
        s=0
        for i in range(n):
            line=map(float,raw_input().split())
            if i==x-1:
                l1=line[y-1]
            s+=sum(line)

        l2=s/n/m
        p1=1-(1-l1)**t
        p2=1-(1-l2)**t
        if p1>p2:
            print 'cc'
            print'%.2f'%p1
        elif p1==p2:
            print 'equal'
            print '%.2f'%p1
        else:
            print 'ss'
            print '%.2f'%p2
    except:
        break
