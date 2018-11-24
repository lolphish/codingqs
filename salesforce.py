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

# Making stack with queue. Push basically adds x and moves it to the top O(n)
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
# Making queue with stack. Have an in and out stack. add into instack and take from out
# when out is empty refill it using instack
class MyQueue(object):
    def __init__(self):
        self.in_stack, self.out_stack = deque(), deque()
    def push(self, x):
        self.in_stack.append(x)
    def pop(self):
        if not self.out_stack:
            self._refill()
        return self.out_stack.pop()
    def peek(self):
        if not self.out_stack:
            self._refill()
        return self.out_stack[-1]
    def empty(self):
        return len(self.in_stack) == len(self.out_stack) == 0
    def _refill(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

# delete duplicate nodes Input: 1->1->2->3->3 Output: 1->2->3 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node != None:
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head

# delete duplicate nodes 2 remove duplicates so only unique nodes
#Input: 1->1->1->2->3 Output: 2->3 
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(-1)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                head = head.next
                pre = pre.next
        return dummy.next

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = deque()
        for n, v in zip(numerals, values):
            res.append((num // v) * n)
            num %= v 
        return ''.join(res)

# House robber 2 (house robber but houses are in a circle)
# basically what it means is that you can either rob starting from 0 to n-1 or start from 1 and go to n 
# Input [2,3,2] Output: 3 since you can't rob 2 and 2
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            now = last = 0
            for i in range(len(nums)):
                now, last = max(nums[i]+last, now), now
            return max(now,last)
        return max(helper(nums[1:]), helper(nums[:-1]))

# calculate operations: 3+2*10/5 = 7
def calculate(self, s):
    stack, num, oper = [], 0, "+"
    operators = {"+","-","*","/"}
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10 + int(s[i])
        if s[i] in operators or i == len(s)-1:
            if oper == "+":
                stack.append(num)
            elif oper == "-":
                stack.append(-num)
            elif oper == "*":
                stack.append(stack.pop()*num)
            elif oper == "/":
                stack.append(int(stack.pop()/num))
            num, oper = 0, s[i]
    return sum(stack)

# Input: "226" Output: 3 since it could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
def numDecodings(self, s):
    if not s:
        return 0
    dp = [0]*(len(s)+1)
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1
    for i in range(2, len(s)+1):
        if s[i-1] != "0":
            dp[i]+= dp[i-1]
        
        val = int(s[i-2:i])
        if val >= 10 and val <= 26:
            dp[i] += dp[i-2]
            
    return dp[len(s)]
# optimized
def numDecodings(self, s):
    if not s:
        return 0
    before_last, last, last_num = 1, (0 if s[0] == "0" else 1), s[0]
    for i in range(1, len(s)):
        cur = 0
        if s[i] != "0":
            cur+= last
        val = int(last_num + s[i])
        if val >= 10 and val <= 26:
            cur += before_last    
        before_last, last, last_num = last, cur, s[i]
    return last