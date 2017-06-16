# coding: utf8
# 用一个栈实现另一个栈的排序
def sortStackByStack(stack):
    Help = []
    while len(stack) > 0:
        cur = stack.pop()
        while len(Help) > 0 and Help[-1] < cur:
            stack.append(Help.pop())
        Help.append(cur)
    while len(Help) > 0:
        stack.append(Help.pop())
    return stack
#
# a = [2,7,4,8,3,7]
# b = sortStackByStack(a)
# print b