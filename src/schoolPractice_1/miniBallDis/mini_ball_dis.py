# -*- coding:utf-8 -*-

class Balls:
    def calcDistance(self, A, B, C, D):
        print 3*(A + B + C + D)

if __name__ == "__main__":
    b = Balls()
    b.calcDistance(100,90,80,70)