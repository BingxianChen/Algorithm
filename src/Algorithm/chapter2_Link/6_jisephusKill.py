# coding: utf8

class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def jisephusKill(head,m):
    if not head or head._next is head or m < 1:
        return head

    last = head
    while last._next is not head:
        last = last._next

    count = 1
    while last._next is not last:
        if count == m:
            last = last._next._next
            count = 0
        else:
            last = last._next
        # head = last._next

        count += 1
    return head

head = Node(1,Node(3,Node(5,Node(8,Node(10)))))
head._next._next._next._next = head

print jisephusKill(head,2).data


