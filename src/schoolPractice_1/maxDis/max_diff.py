
class LongestDistance:
    def getDis(self, A, n):
        maxdis = 0
        for a in range(n):
            for b in range(a,n):
                if maxdis < A[b] - A[a]:
                    maxdis = A[b] - A[a]
        return maxdis

if __name__=="__main__":
    l = LongestDistance()
    print l.getDis([5386,5384,11054,6345,5816,11757],6)