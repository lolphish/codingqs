class PairListNode:
    def __init__(self, k,v):
        self.pair = (k,v)
        self.next = None
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.map = [None]*self.buckets
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        id = key % self.buckets
        if not self.map[id]:
            self.map[id] = PairListNode(key,value)
        else:
            cur = self.map[id]
            while True:
                if cur.pair[0] == key: # update
                    cur.pair = (key,value)
                    return
                elif not cur.next:
                    break
                cur = cur.next
            cur.next = PairListNode(key,value)
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        id = key % self.buckets
        cur = self.map[id]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            cur = cur.next
        return -1
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        id = key % self.buckets
        if self.map[id] and self.map[id].pair[0] == key:
            self.map[id] = self.map[id].next
            return
        cur = self.map[id]
        while cur and cur.next:
            if cur.next.pair[0] == key:
                cur.next = cur.next.next
            cur = cur.next

# Making stack with queue
from collections import deque
class MyStack:
    def __init__(self):
        self.queue = deque()
    def push(self, x):
        q = self.queue # for cleanliness
        q.appendleft(x)
        for _ in range(len(q) - 1):
            q.appendleft(q.pop())
    def pop(self):
        return self.queue.pop()
    def top(self):
        return self.queue[-1]
    def empty(self):
        return not len(self.queue)