# coding: utf8

# 删除无序单链表中值重复出现的节点
class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def removeRep(head):
    if not head:
        return Node

    duplicate = set()
    pre = head
    cur = head._next
    duplicate.add(head.data)
    while cur:
        if cur.data in duplicate:
            pre._next = cur._next
        else:
            duplicate.add(cur.data)
            pre = cur
        cur = cur._next

    return head

head = Node(1,Node(3,Node(3,Node(8,Node(10)))))
a = removeRep(head)
print a