# Remove Invalid Parentheses (Facebook)
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
                    found = True
                    res.append(cur_str)

                if found:
                    continue
                
                for i in range(len(cur_str)):
                    if cur_str[i] != "(" and cur_str[i] != ")":
                        continue
                    new_str = cur_str[:i]+cur_str[i+1:]
                    if new_str not in visited:
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