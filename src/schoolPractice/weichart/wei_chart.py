# -*- coding:utf-8 -*-

class Gift:
    def getValue(self, gifts, n):
        record = dict()
        for i in gifts:
            record[i] = record.get(i,0) + 1
            if record[i] > n/2:
                return i
        return 0

if __name__ == "__main__":
    g = Gift();
    print g.getValue([1,2,3,2,2],5)