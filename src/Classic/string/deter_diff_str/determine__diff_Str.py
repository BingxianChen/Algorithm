# -*- coding:utf-8 -*-
class Different:
    def checkDifferent(self, iniString):
        for i in xrange(len(iniString) - 1):
            for j in xrange(i + 1,len(iniString)):
                if iniString[i] == iniString[j]:
                    return False
        return True

if __name__ == "__main__":
    d = Different()
    print d.checkDifferent("fbcdbea")