import sys
while True:
    try:
        line1 = sys.stdin.readline().strip(" ").split()
        N = int(line1[0])
        M = int(line1[1])
        score = [int(k) for k in sys.stdin.readline().strip(" ").split()]
        if len(score) == N and 0 < N <= 30000 and 0 <= M < 5000:
            for i in range(M):
                qoru = sys.stdin.readline().strip(" ").split()
                if qoru[0] is 'Q':
                    a = int(qoru[1])
                    b = int(qoru[2])
                    if a <= b:
                        print max(score[a - 1:b])
                    else:
                        print max(score[b - 1:a])
                if qoru[0] is 'U':
                    score[int(qoru[1]) - 1] = int(qoru[2])
    except:
        break