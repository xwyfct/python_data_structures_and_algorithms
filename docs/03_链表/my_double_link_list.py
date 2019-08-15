#!/usr/bin/python
# -*- coding:utf8 -*-


class Node:

    def __init__(self, prev=None, next=None, value=None):
        self.prev = prev
        self.next = next
        self.value = value
    

class CircularDoubleLinkedList:

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev, node.next = node, node
        self.root = node
        self.length = 0
    
    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception("full error")
        node = Node(value=value)
        tailnode = self.tailnode() or self.root
        
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node

        self.length += 1
    
    def appendleft(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception("full error")
        node = Node(value=value)
        if self.root.next == self.root:# empty
            self.root.next = node
            self.root.prev = node
            node.next = self.root
            node.prev = self.root
        else:
            headnode = self.headnode()
            self.root.next = node
            node.prev = self.root
            node.next = headnode
            headnode.prev = node

        self.length += 1
    
    def remove(self, node):
        if node is self.root:
            return -1
        else:
            prevnode = node.prev
            nextnode = node.next
            prevnode.next = nextnode
            nextnode.prev = prevnode
        self.length -= 1
    
    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode is not self.root:
            yield curnode
            curnode = curnode.next
    
    def __iter__(self):
        if self.root.next is self.root:
            return
        for node in self.iter_node():
            yield node.value
    
    def iter_node_reverse(self):
        if self.root.next is self.root:
            return
        curnode = self.root.prev
        while curnode is not self.root:
            yield curnode
            curnode = curnode.prev


def test_dll_append():
    dll = CircularDoubleLinkedList()
    dll.append(0)
    dll.append(1) 
    assert dll.length == 2

def test_dll_appendleft():
    dll = CircularDoubleLinkedList()
    dll.append(0)
    dll.append(1)
    assert dll.length == 2

def test_dll_remove():
    dll = CircularDoubleLinkedList()
    dll.append(0)
    dll.append(1)
    node = dll.headnode()
    dll.remove(node)
    assert dll.length == 1

def test_dll_iter_node():
    dll = CircularDoubleLinkedList()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.iter_node()

def test_dll_iter():
    dll = CircularDoubleLinkedList()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    for value in dll:
        print(value)

def test_dll_iter_node_reverse():
    dll = CircularDoubleLinkedList()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.iter_node_reverse()

if __name__ == "__main__":
    test_dll_append()
    test_dll_appendleft()
    test_dll_remove()
    test_dll_iter_node()
    test_dll_iter_node_reverse()
    test_dll_iter()



        
        

