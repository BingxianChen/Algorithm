# coding: utf8

class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next


def removeLastKthNode(head, lastKth):
    if head.data is None or lastKth < 1:
        return head
    cur = head
    while cur._next is not None:
        lastKth -= 1
        cur = cur._next

    lastKth +=1
    if lastKth == 0:
        head = head._next
    if lastKth < 0:
        lastKth +=1
        while lastKth != 0:
            head = head._next
            lastKth +=1
        head._next = head._next._next
    return head

head = Node(1,Node(3,Node(5,Node(8,Node(10)))))
k = 2

a = removeLastKthNode(head,k)
print a._next.data