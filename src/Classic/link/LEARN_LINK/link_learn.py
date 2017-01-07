# -*- coding:utf-8 -*-

class Node:
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    #删除一个节点之后记得要把链表长度减一
    def delete(self, index):
        if self.isEmpty():
            print "this chain table is empty."
            return

        if index < 0 or index >= self.length:
            print 'error: out of index'
            return
        #要注意删除第一个节点的情况
        #如果有空的头节点就不用这样
        #但是我不喜欢弄头节点
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        #prev为保存前导节点
        #node为保存当前节点
        #当j与index相等时就
        #相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print 'error: out of index'
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print "error: out of index"
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print "this chain table is empty"
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print "%s not found" % str(data)
            return

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print "this chain tabale is empty"
            return

        if index < 0 or index >= self.length:
            print "error: out of index"
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def clear(self):
        self.head = None
        self.length = 0

L = Node('a')
L.next = Node('b')
b = L.next
c = Node('c')
b.next = c
print L.next.next


