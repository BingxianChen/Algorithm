# -*- coding:utf-8 -*-
class Joseph:
    def getResult(self, n):
        A = range(1,n+1)
        count = 2
        while len(A) > 1:
            for i in xrange(len(A)):
                if i%count != 0:
                    A[i] = None
            while True:
                try:
                    index = A.index(None)
                    A.pop(index)
                except:
                    break
            A.insert(0,A[len(A) - 1])
            A.pop()
            count += 1
        return A[0]

if __name__=="__main__":
    j = Joseph()
    j.getResult(5)