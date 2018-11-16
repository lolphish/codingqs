class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = deque()
        self.backtrack(n, res, [], 0, 0)
        return list(res)
        
    
    def backtrack(self, n, res, cur, opn_paren, closed_paren):
        if len(cur) == n*2:
            res.append("".join(cur))
            return
        if opn_paren < n:
            cur.append("(")
            self.backtrack(n,res, cur, opn_paren+1, closed_paren)
            cur.pop()
        if closed_paren < opn_paren:
            cur.append(")")
            self.backtrack(n,res, cur, opn_paren, closed_paren+1)
            cur.pop()

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