class GoUpstairs:
    def countWays(self, n):
        s0=1
        s1=2
        if n==1:
            step = 0
        elif n==2:
            step = 1
        elif n==3:
            step = 2
        else:
            for i in range(4,n+1):
                step = (s0+s1)%1000000007
                s0 = s1
                s1 = step
        return step

if __name__ == "__main__":
    c = GoUpstairs()
    print c.countWays(3)
