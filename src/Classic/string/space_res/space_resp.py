# -*- coding:utf-8 -*-
class Replacement:
    def replaceSpace(self, iniString, length):
        return "%20".join(iniString.split(" "))

if __name__ == "__main__":
    r =Replacement()
    print r.replaceSpace("a   b",5)