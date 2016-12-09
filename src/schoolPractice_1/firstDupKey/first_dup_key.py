# -*- coding:utf-8 -*-

class FirstRepeat:
    def findFirstRepeat(self, A, n):
        B = set()
        for a in A:
            if a not in B:
                B.add(a)
            else:
                return a

if __name__ == "__main__":
    f = FirstRepeat()
    print f.findFirstRepeat("qywyer23tdd",11)