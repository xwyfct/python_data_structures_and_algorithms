#!/usr/bin/python
# -*- coding:utf8 -*-
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity=128):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key, default=None):
        val = self.od.get(key, default)
        self.od.move_to_end(key)
        return val

    def add_or_update(self, key, value):
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
        else:
            self.od[key] = value # insert to end
            if len(self.od) > self.capacity:
                self.od.popitem() # delete first item

    def __call__(self, func):
        def _(n):
            if n in self.od:
                value = self.get(n)
                return value
            else:
                val = func(n)
                self.add_or_update(n, val)
                return val
        return _

@LRUCache(256)
def f_use_lru(n):
    if n <= 1:
        return n
    else:
        return f_use_lru(n-1) + f_use_lru(n-2)

def test():
    import time
    beg = time.time()
    for i in range(34):
        print(f_use_lru(i))
    print(time.time() - beg)


if __name__ == "__main__":
    test()


