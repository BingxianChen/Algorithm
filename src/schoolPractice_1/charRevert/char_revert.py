# -*- coding:utf-8 -*-

class StringRotation:
    def rotateString(self, A, n, p):
        return A[p+1:] + A[:p+1]

if __name__ == "__main__":
    s = StringRotation()
    print s.rotateString("ABCDEFGH",8,4)