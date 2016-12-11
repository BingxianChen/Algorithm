# -*- coding:utf-8 -*-
import collections
class Coder:
    def findCoder(self, A, n):
        order_dic = collections.OrderedDict()
        for i in range(0,n):
            count = A[i].lower().count("coder")
            if count != 0:
                order_dic[A[i]] = count
        B = sorted(order_dic.items(),key=lambda x:x[1],reverse=True)
        C = []
        for index in B:
            C.append(index[0])
        print C

if __name__ == "__main__":
    c = Coder()
    c.findCoder(["i am a coder","Coder Coder","Code"],3)