# coding: utf8
# 一种奇怪的节点删除方式

class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def removeNodeWired(node):
    if not node:
        return
    cur_next = node._next
    if not cur_next:
        raise "can not remove last node"
    node.data = cur_next.data
    node._next = cur_next._next

    return node

head = Node(1,Node(3,Node(3,Node(8,Node(10)))))
node = head._next._next

a = removeNodeWired(node)
print a