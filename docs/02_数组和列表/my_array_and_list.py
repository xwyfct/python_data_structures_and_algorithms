#!/usr/bin/python
# -*- coding:utf8 -*-


class Array:

    def __init__(self, size=10):
        self.size = size
        self._items = [None] * size
    
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __len__(self):
        return self.size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value
    
    def __iter__(self):
        for item in self._items:
            yield item

            
def test_array():
    array = Array()
    array[0] = 1
    assert array[0] == 1
    assert len(array) == 10
    array.clear()
    assert array[0] == None


