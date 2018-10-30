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


class DoubleLinkedNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = DoubleLinkedNode(None, None)
        self.tail = DoubleLinkedNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.dic:
            return -1
        res = self.dic[key]
        self._remove(res)
        self._insert(res)
        return res.value
        

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
            del self.dic[key]
        elif len(self.dic) >= self.capacity:
            del self.dic[self.tail.prev.key]
            self._remove(self.tail.prev)
        new_node = DoubleLinkedNode(key, value)        
        self.dic[key] = new_node
        self._insert(new_node)

    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
