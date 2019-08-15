#!/usr/bin/python
# -*- coding:utf8 -*-


class Node:
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList:

    def __init__(self, maxsize=None):
        self.length = 0
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
    
    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception("linked list is full")
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1
    
    def appendleft(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception("linked list is full")
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node
        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1
    
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    
    def iter_node(self):
        currnode = self.root.next
        while currnode:
            yield currnode
            currnode = currnode.next
    
    def remove(self, value):
        prenode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prenode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prenode
                del curnode
                self.length -= 1
                return 1
            else:
                prenode = curnode
        return -1

    def find(self, value):
        index = 0
        for v in self:
            if v == value:
                return index
            index += 1
        return -1
    
    def popleft(self):
        if self.tailnode is None:
            raise Exception("linked list is empty")
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        self.length -= 1
        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.length = 0
        self.root.next = None
        self.tailnode = None
    
    def reverse(self):
        curnode = self.root.next
        self.tailnode = curnode
        prevnode = None
        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode
            prevnode = curnode
            curnode = nextnode
    
def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    print(list(ll))
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_remove()
    test_linked_list_reverse()


    
    





