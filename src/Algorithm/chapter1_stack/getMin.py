# coding:utf-8
# 实现一个特殊的栈,在实现栈的基本功能的基础上,再实现返回栈中最小元素的操作
# book Num.1.1
class getMin():
    stackData = []
    stackMin = []

    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self,newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0:
            self.stackMin.append(newNum)
        elif newNum <= self.stackMin[-1]:
            self.stackMin.append(newNum)
        else:
            self.stackMin.append(self.stackMin[-1])

    def pop(self):
        if len(self.stackData)==0:
            raise "Your stack is empty!"
        self.stackMin.pop()
        return self.stackData.pop()

    def getmin(self):
        if len(self.stackMin)==0:
            raise "Your stack is empty!"
        return self.stackMin[-1]
