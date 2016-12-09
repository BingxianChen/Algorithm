# -*- coding:utf-8 -*-

class BinarySearch:
    def getPos(self, A, n, val):
        k = 0
        for i in A:
            if i == val:
                return k
            k += 1

if __name__== "__main__":
    b = BinarySearch()
    print b.getPos([1,3,5,7,9],5,3)