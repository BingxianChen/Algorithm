# -*- coding:utf-8 -*-
class Printer:
    def printMatrix(self, mat, n, m):
        A = []
        for i in range(0,n):
            for j in range(0,m):
                if i % 2 == 1:
                    A.append(mat[i][m-j-1])
                else:
                    A.append(mat[i][j])
        return A
if __name__ == "__main__":
    p = Printer()
    print p.printMatrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],4,3)