class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False
                
    
    def dfs(self, board, word, x, y):
        if board[x][y] == word[0]:
            if not word[1:]:
                return True
            temp, board[x][y] = board[x][y], "#"
            if x > 0 and self.dfs(board, word[1:], x-1, y):
                return True
            if x < len(board)-1 and self.dfs(board,word[1:], x+1, y):
                return True
            if y > 0 and self.dfs(board, word[1:], x, y-1):
                return True
            if y < len(board[0])-1 and self.dfs(board,word[1:], x, y+1):
                return True
            board[x][y] = temp
        return False