# -*- coding:utf-8 -*-
class Joseph:
    def getResult(self, n, m):
        A = range(1,n+1)
        i = 0
        while len(A) > 1:
            i = (i + m -1)%len(A)
            A.remove(A[i])
        return A[0]
if __name__ == "__main__":
    j = Joseph()
    print j.getResult(5,3)