# coding: utf8

# 二叉树的序列化与反序列化
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def serialBypre(head):
    if not head:
        return "#!"
    res = str(head.data) + "!"
    res += serialBypre(head.left)
    res += serialBypre(head.rigth)
    return res

def reconByPreString(serial):
    values = serial.split("!")
    values.pop()
    values.reverse()
    return reconPreOrder(values)

def reconPreOrder(values):
    value = values.pop()
    if value is "#":
        return None
    head = Node(int(value))
    head.left = reconPreOrder(values)
    head.rigth = reconPreOrder(values)
    return head



head = Node(1,Node(23))
a = reconByPreString("1!23!#!#!#!")
print a
print serialBypre(a)