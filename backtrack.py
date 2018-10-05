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