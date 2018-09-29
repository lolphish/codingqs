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