# coding: utf8

# 判断T1树是否包含T2树全部的拓扑结构
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def contain(t1, t2):
    return check(t1,t2) or contain(t1.left,t2) or contain(t1.right,t2)

def check(h,t2):
    if t2 is None:
        return True
    if h is None or h.data is not t2.data:
        return False
    return check(h.left,t2.left) and check(h.right,t2.right)

t1 = Node(1,Node(23))
t2 = Node(1)

print contain(t1,t2)