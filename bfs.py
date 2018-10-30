# Remove Invalid Parentheses (Facebook) # Least amount of parentheses removed to make it valid
# Example 1: Input: "()())()" Output: ["()()()", "(())()"] 
# Example 2: Input: "(a)())()" Output: ["(a)()()", "(a())()"]
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str] 
        """
        def bfs():
            visited = set()
            found = False
            res, q = collections.deque(), collections.deque()
            q.append(s)
            while q:
                cur_str = q.popleft()

                if self.validParentheses(cur_str): 
                    found = True # if this (number of) depth of parentheses makes a valid, then stop the bfs
                    res.append(cur_str)

                if found: # already at least amount of parentheses removed so stops the bfs
                    continue
                
                for i in range(len(cur_str)): # tries removing each parentheses and add to queue
                    if cur_str[i] != "(" and cur_str[i] != ")":
                        continue
                    new_str = cur_str[:i]+cur_str[i+1:]
                    if new_str not in visited: # pruning/optimizing by visited set
                        visited.add(new_str)
                        q.append(new_str)
            return list(res)
        return bfs()
        
    def validParentheses(self, s):
        counter = 0
        for paren in s:
            if paren == "(":
                counter+=1
            else:
                counter -= (paren == ")")
                if counter == -1:
                    return False
        return counter == 0

    # backtracking problem permutations
    class Solution:
        def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, used = [], [False]*len(nums)
        # sort(nums) if there are duplicate numbers
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append([n for n in cur])
            else:
                for i in range(len(nums)):
                    if used[i]: # if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1])
                        continue
                        used[i] = True
                        cur.append(nums[i])
                        
                        backtrack(cur)
                        
                        cur.pop()
                        used[i] = False
            
                    
        backtrack([])
        return res

# Nested Weighted List Sum
# Input: [1,[4,[6]]] Output: 27. 1 in depth 1 + 4*depth2 + 6*depth3
def depthSum(self, nestedList):
    res, depth = 0, 1
    while nestedList:
        tempList = deque()
        for i in nestedList:
            if i.isInteger():
                res += i.getInteger()*depth
            else:
                tempList.extend([j for j in i.getList()])
        nestedList, depth = tempList, depth+1
    return res
            
# Nested Weibghted List Sum II
# Input: [1,[4,[6]]] Output: 17 Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
def depthSumInverse(self, nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    depthQueue, depth = deque(), 1
    while nestedList:
        tmpList, res = deque(), 0
        for obj in nestedList:
            if obj.isInteger():
                res+= obj.getInteger()
            else:
                tmpList.extend([i for i in obj.getList()])
        depthQueue.append(res)
        nestedList, depth = tmpList, depth+1
    res, depth = 0, depth-1
    for num in depthQueue:
        res+= num*depth
        depth-=1
    return res
    # more efficient way by just repeat adding every layer
    res, unweighted = 0, 0
    while nestedList:
        tmpList = deque()
        for obj in nestedList:
            if obj.isInteger():
                unweighted+=obj.getInteger()
            else:
                tmpList.extend([i for i in obj.getList()])
        res+=unweighted
        nestedList = tmpList
    return res