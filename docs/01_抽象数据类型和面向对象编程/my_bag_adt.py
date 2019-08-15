#!/usr/bin/python
# -*- coding:utf8 -*-


class Bag(object):

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()
    
    def add(self, item):
        if len(self) > self.maxsize:
            raise Exception("full")
        self._items.append(item)
    
    def remove(self, item):
        if item not in self._items:
            raise Exception("item not exist")
        self._items.remove(item)
    
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item
    
def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert len(bag) == 3
    bag.remove(2)
    bag.remove(4)
    assert len(bag) == 2
    for item in bag:
        print(item)

if __name__ == "__main__":
    test_bag()
