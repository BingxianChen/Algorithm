# -*- coding:utf-8 -*-
class Reverse:
    def reverseString(self, iniString):
        return iniString[::-1]

if __name__ == "__main__":
    r = Reverse()
    print r.reverseString("This is nowcoder")