# -*- coding:utf-8 -*-

class GrayCode:
    def getGray(self, n):
        if n == 0:
            return ["0"]
        elif n == 1:
            return ["0", "1"]
        else:
            res = self.getGray(n - 1)
            mylen = len(res)
            for i in range(mylen - 1, -1, -1):
                res.append('1' + res[i])
            for i in range(0, mylen):
                res[i] = "0" + res[i]
            return res