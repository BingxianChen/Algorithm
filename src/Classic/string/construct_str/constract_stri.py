# -*- coding:utf-8 -*-
class Same:
    def checkSam(self, stringA, stringB):
        return set(stringA) == set(stringB)

if __name__ == "__main__":
    s = Same()
    print s.checkSam("This is nowcoder","is This nowcoder")
    print s.checkSam("Here you are","Are you here")