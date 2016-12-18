class MaxInnerRec:
    def countArea(self, A, n):
        Max = 0
        before = 0
        after = 0
        for i in range(0,n):
            for b in range(i,-1,-1):
                if A[b] < A[i]:
                    before = b
                    break
                if b == 0:
                    before = -1
            for a in range(i,n):
                if A[a] < A[i]:
                    after = a
                    break
                if a == n-1:
                    after = n
            if Max < A[i] * (after - before - 1):
                Max = A[i] * (after - before - 1)
        return Max

if __name__ == "__main__":
    m = MaxInnerRec()
    print m.countArea([691,611,664,535],4)