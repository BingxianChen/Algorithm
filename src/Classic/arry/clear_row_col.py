# -*- coding:utf-8 -*-
class Clearer:
    def clearZero(self, mat, n):
        row = []
        col = []
        for i in xrange(n):
            for j in xrange(n):
                if mat[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in xrange(n):
            for j in xrange(n):
                if i in row or j in col:
                    mat[i][j] = 0

        return mat


if __name__ == "__main__":
    c = Clearer()
    mat = c.clearZero([[1,2,3],[0,1,2],[0,0,1]],3)
    print mat






##################################
# 题目描述
# 请编写一个算法，若N阶方阵中某个元素为0，则将其所在的行与列清零。
# 给定一个N阶方阵int[][](C++中为vector>)mat和矩阵的阶数n，请返回完成操作后的int[][]方阵(C++中为vector>)，保证n小于等于300，矩阵中的元素为int范围内。

# 测试样例：
# [[1,2,3],[0,1,2],[0,0,1]]

# 返回：[[0,0,3],[0,0,0],[0,0,0]]