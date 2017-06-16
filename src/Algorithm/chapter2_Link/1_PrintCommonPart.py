# coding: utf8

# 打印两个有序链表的公共部分
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self._next = next

def printCommonPart(head1,head2):
    print "Common Part:"
    while head1._next is not None and head2._next is not None:
        if head1.data < head2.data:
            head1 = head1._next
        elif head1.data > head2.data:
            head2 = head2._next
        else:
            print head1.data
            head1 = head1._next
            head2 = head2._next
    print " "

head1 = Node(1,Node(3,Node(5,Node(8,Node(10)))))
head2 = Node(2,Node(3,Node(6,Node(8,Node(11)))))

printCommonPart(head1,head2)
