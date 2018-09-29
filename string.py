from collections import Counter, deque, defaultdict
def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

''' [1,3,-1,-3,5,3,6,7] and 3 will return [-1, -3, -3, -3, -3, 5]'''
def slidingWindowMin(s:list, w:int):
    d = deque()
    res = []
    for i, n in enumerate(s):
        while d and s[d[0]] > n: # pop any smaller than current n, max pops < n
            d.popleft()
        d.append(i)
        if d and d[0] < i - w: #
            d.popleft()
        if i >= w - 1: # only start adding when there are k numbers
            res.append(s[d[0]])
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

def areSentencesSimilar(words1, words2, pairs):
    if len(words1) != len(words2):
        return False
    words = defaultdict(set)
    # Build the graph from pairs.
    for w1, w2 in pairs:
        words[w1].add(w2)
        words[w2].add(w1)

    similar_words = {}

    # dfs to make every word correspond to the same root words
    def dfs(word, root_word): # if it's already been added with a root word, do nothing
        if word in similar_words:
            return
        similar_words[word] = root_word
        for synonym in words[word]: # make all synonyms in dict use the same root word
            dfs(synonym, root_word)

    # Assign root words.
    for word in words:
        dfs(word, word)

    # Compare words.
    return all(similar_words.get(w1, w1) == similar_words.get(w2, w2) for w1, w2 in zip(words1, words2))

def lengthLongestPath(input):
    currlen, maxlen = 0, 0  # running length and max length
    stack = []  # keep track of the name length
    for s in input.split('\n'):
        print(s)
        print(stack)
        depth = s.count('\t')  # the depth of current dir or file
        while len(stack) > depth:  # go back to the correct depth
            currlen -= stack.pop()
        stack.append(len(s.strip('\t')) + 1)  # 1 is the length of '/'
        currlen += stack[-1]  # increase current length
        if '.' in s:  # update maxlen only when it is a file
            maxlen = max(maxlen, currlen - 1)  # -1 is to minus one '/'
    return maxlen

def wordfitting(sentence, rows, cols):
    s = " ".join(sentence) + " "
    start, n = 0, len(s)  # start will keep repeatedly going through s
    for i in range(0, rows):
        start += cols
        if s[start % n] == " ": # we dont need extra space for current row
            start += 1
        else:
            while start > 0 and s[(start - 1) % n] != " ": # go backwards until a space " "
                start -= 1
    return start / n

''' 
group shifted strings: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"] to
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
def groupStrings(self, strings):
    groups = defaultdict(list)
    for s in strings:
        groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
    return groups.values()



'''
s = "abpcplea", d = ["ale","apple","monkey","plea"]
output = "apple"
'''
def findLongestWord(self, S, D):
    D.sort(key = lambda x: (-len(x), x))
    for word in D:
        i = 0
        for c in S:
            if i < len(word) and word[i] == c:
                i += 1
        if i == len(word):
            return word
    return ""

def findLongestWord(self, s, d):
    def isSubsequence(x):
        it = iter(s)
        return all(c in it for c in x)
    return min(filter(isSubsequence, d) + [''], key=lambda x: (-len(x), x))


'''
abbrev

'''
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result


if __name__ == "__main__":
    print(slidingWindowMin([1,3,-1,-3,5,3,6,7],3))
    print(minWindowSubstring("ADOBECODEBANC", "ABC"))
    print(longestSubstringWithoutRepeat("pwwkew"))
    print(longestSubstringTwoDistinct("eceba"))
    print(lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
