# -*- coding:utf-8 -*-

class Flip:
    def flipChess(self, A, f):
        for k in range(0,3):
            for i in range(-1,2,2):
                try:
                    if f[k][0] + i - 1 < 0 or f[k][1] - 1 < 0:
                        continue
                    A[f[k][0] + i - 1][f[k][1] - 1] = (A[f[k][0] + i - 1][f[k][1] - 1] + 1) % 2
                except:
                    continue
            for j in range(-1,2,2):
                try:
                    if f[k][0] - 1 < 0 or f[k][1] + j - 1 < 0:
                        continue
                    A[f[k][0] - 1][f[k][1] + j - 1] = (A[f[k][0] - 1][f[k][1] + j - 1] + 1) % 2
                except:
                    continue
        return A
if __name__ == "__main__":
    f = Flip()
    print f.flipChess([[0,1,0,0],[1,0,1,0],[1,1,0,0],[1,0,0,1]],[[2,3],[4,2],[2,3]])


