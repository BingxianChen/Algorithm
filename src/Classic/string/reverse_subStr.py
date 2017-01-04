# -*- coding:utf-8 -*-
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        for i in xrange(len(s1)):
            if s1[i:] + s1[:i] == s2:
                return True
        return False

if __name__ == "__main__":
    r = ReverseEqual()
    print r.checkReverseEqual("waterbottle","erbottlewat")



# ##########################
# 题目描述
# 假定我们都知道非常高效的算法来检查一个单词是否为其他字符串的子串。请将这个算法编写成一个函数，给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成，要求只能调用一次检查子串的函数。
# 给定两个字符串s1,s2,请返回bool值代表s2是否由s1旋转而成。字符串中字符为英文字母和空格，区分大小写，字符串长度小于等于1000。
# 测试样例：
# "Hello world","worldhello "
# 返回：false
# "waterbottle","erbottlewat"
# 返回：true