
''' [1,3,-1,-3,5,3,6,7] and 3 will return [-1, -3, -3, -3, -3, 5]'''
def slidingWindowMin(s:list, w:int):
    d = deque()
    res = []
    for i, n in enumerate(s):
        while d and s[d[0]] > n: # pop any smaller than current n, max pops < n
            d.popleft()
        d.append(i)
        if d and d[0] < i - w: # out of window range
            d.popleft()
        if i >= w - 1: # only start adding when there are k numbers
            res.append(s[d[0]])
    return res

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = deque()
        st = deque()
        for i in range(len(nums)):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            st.append(i)
            if st[0] == i - k:
                st.popleft()
            if i >= k - 1:
                res.append(nums[st[0]])
        return list(res)
        
# Input: s: "cbaebabacd" p: "abc" Output: [0, 6] (Facebook Problem)

from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res, c = [], Counter(p)
        begin, end, counter = 0,0, len(c)
        while end < len(s):
            if s[end] in c:
                c[s[end]]-=1
                if c[s[end]] == 0:
                    counter-=1
            end+=1
            while counter == 0:
                if s[begin] in c:
                    c[s[begin]]+=1
                    if c[s[begin]] > 0:
                        counter+=1
                        
                if end-begin == len(p):
                    res.append(begin)
                begin+=1
        return res

# Substring problems template (anything given a string and pattern)
'''str = ADOBECODEBANC, T = abc'''
def minWindowSubstring(s:str, pat:str):
    c = Counter(pat)
    counter = len(c)
    begin, end = 0, 0 # two pointers to move the window
    length, head = float("inf"), 0 # length for checking min, head is pointer to front
    while end < len(s):
        if s[end] in c:
            c[s[end]] = c[s[end]] - 1
            if c[s[end]] == 0:
                counter-=1
        end+=1
        while counter == 0: # if condition matches
            if s[begin] in c:
                c[s[begin]] = c[s[begin]] + 1
                if c[s[begin]] > 0:
                    counter+=1
            if end-begin < length:
                length = end - begin
                head = begin
            begin+=1
    return "" if length == float("inf") else s[head:head+length]

''' str = "abcabcbb" = "abc", str="pwwkew" = "wke"'''
def longestSubstringWithoutRepeat(s:str):
    begin, end, longest = 0, 0, 0
    st = set()
    while end < len(s):
        if s[end] not in st:
            st.add(s[end])
            longest = max(longest, len(st))
            end+=1
        else:
            st.remove(s[begin])
            begin+=1
    return longest

''' str = "eceba" = "ece"'''
def longestSubstringTwoDistinct(s:str):
    begin, end, length = 0, 0, 0
    c = Counter()
    counter = 0
    while end < len(s):
        c[s[begin]] = c[s[begin]] + 1
        if c[s[begin]] == 1:
            counter+=1
        end+=1
        while counter > 2:
            c[s[begin]] = c[s[begin]] - 1
            if c[s[begin]] == 0:
                counter-=1
            begin+=1
        length = max(length, end-begin)
    return length