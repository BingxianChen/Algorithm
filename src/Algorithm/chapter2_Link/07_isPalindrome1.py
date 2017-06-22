# coding: utf8

# 判断链表是否是回文结构
class Node(object):
    def __init__(self,data,_next=None):
        self.data = data
        self._next = _next

def isPalindrome1(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur.data)
        cur = cur._next

    while head:
        if head.data != stack.pop():
            return False
        else:
            head = head._next

    return True


head = Node(1,Node(3,Node(5,Node(3,Node(1)))))
print isPalindrome1(head)