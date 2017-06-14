# coding:utf8
# 由两个栈组成的队列
# 编写一个类,用两个栈实现队列,支持队列的基本操作(add,poll,peek)

class TwoStacksQueue():

    def __init__(self):
        self.stackpush = []
        self.stackpop = []

    def add(self,pushInt):
        self.stackpush.append(pushInt)

    def poll(self):
        if len(self.stackpush)==0 and len(self.stackpop)==0:
            raise "Queue is empty!"
        elif len(self.stackpop)==0:
            while len(self.stackpush) != 0:
                self.stackpop.append(self.stackpush.pop())

        return self.stackpop.pop()

    def peek(self):
        if len(self.stackpush)==0 and len(self.stackpop)==0:
            raise "Queue is empty!"
        elif len(self.stackpop)==0:
            while len(self.stackpush) != 0:
                self.stackpop.append(self.stackpush.pop())

        return self.stackpop[-1]

