import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

while True:
    try:
        line1 = sys.stdin.readline().strip(" ").split()
        n = int(line1[0])
        a = int(line1[1])
        line2 = [int(i) for i in sys.stdin.readline().strip(" ").split()]
        if len(line2) == 1:
            for i in range(n - 1):
                line2.append(int(sys.stdin.readline().strip(" ")))
        for b in line2:
            if b <= a:
                a += b
            else:
                a += gcd(a,b)
        print a
    except:
        break