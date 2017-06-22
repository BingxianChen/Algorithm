# coding: utf8

# 两个单链表生成相加链表
class Node(object):
    def __init__(self,data,_next = None):
        self.data = data
        self._next = _next

def addList(head1,head2):
    s1 = []
    s2 = []
    while head1:
        s1.append(head1.data)
        head1 = head1._next
    while head2:
        s2.append(head2.data)
        head2 = head2._next

    ca = 0
    n1 = 0
    n2 = 0
    n = 0
    node = None
    pre = None
    while s1 or s1 :
        n1 = s1.pop() if s1 else 0
        n2 = s2.pop() if s2 else 0
        n = n1 + n2 + ca
        pre = node
        node = Node(n%10)
        node._next = pre
        ca = n/10

    if ca == 1:
        pre = node
        node = Node(1)
        node._next = pre

    return node

head1 = Node(9,Node(3,Node(7)))
head2 = Node(6,Node(3))

a = addList(head1,head2)
print a