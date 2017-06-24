# coding: utf8
# 向有序的环形单链表中插入新节点

class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def insertNum(head,num):
    node = Node(num)
    if not head:
        node._next = node
        return node
    pre = head
    cur = head._next
    while cur is not head:
        if pre.data <= num and cur.data >= num:
            break
        pre = cur
        cur = cur._next

    pre._next = node
    node._next = cur
    return head if head.data < num else node

head = Node(2,Node(3,Node(3,Node(8,Node(10)))))
head._next._next._next._next._next = head

a = insertNum(head,5)
print a