while True:
    try:
        a = int(raw_input())
        b = [int(i) for i in raw_input().strip().split()]

        print a
        print b
    except:
        break