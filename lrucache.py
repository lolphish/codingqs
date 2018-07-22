import collections
class lrucache:
    def __init__(self, capacity):
        self.deque = collections.deque([])
        self.dic = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def set(self, key, value):
        if key in self.dic:
            self.deque.remove(key)
        elif len(self.dic) == self.capacity:
            v = self.deque.popleft()  # remove the Least Recently Used element
            self.dic.pop(v)
        self.deque.append(key)
        self.dic[key] = value