# coding: utf8

class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def removeMidNode(head):
    if not head or not head._next:
        return head
    if not head._next._next:
        return head._next
    pre = head
    cur = head._next._next
    while cur._next and cur._next._next:
        pre = pre._next
        cur = cur._next._next
    pre._next = pre._next._next
    return head




# head = Node(1,Node(3,Node(5,Node(8,Node(10)))))
# a = removeMidNode(head)
# print a