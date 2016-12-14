# -*- coding:utf-8 -*-

class Rotate:
    def rotateMatrix(self, mat, n):
        A = [[] for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(0,n):
                A[j].append(mat[i][j])
        return A

if __name__ == "__main__":
    r = Rotate()
    print r.rotateMatrix([[1,2,3],[4,5,6],[7,8,9]],3)