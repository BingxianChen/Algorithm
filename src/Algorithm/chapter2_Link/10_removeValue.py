# coding: utf8

# 在单链表中删除指定值得节点
class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def removeValue(head,num):
    while head:
        if head.data != num:
            break
        head = head._next

    pre = head
    cur = head._next
    while cur:
        if cur.data == num:
            pre._next = cur._next
        else:
            pre = cur
        cur = cur._next

    return head

head = Node(1,Node(3,Node(3,Node(8,Node(10)))))
a = removeValue(head,3)
print a