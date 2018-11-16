# Word Search: given a crossword: find if a word exist
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        M, N = len(board), len(board[0])
        def dfs(x,y, word_index):
            if board[x][y] == word[word_index] :
                if word_index+1 >= len(word):
                    return True
                temp, board[x][y] = board[x][y], "#"
                for dx,dy in ((-1,0), (0,-1), (1,0), (0,1)):
                    if 0 <= x+dx < M and 0 <= y+dy < N and dfs(x+dx, y+dy, word_index+1):
                        return True
                board[x][y] = temp
            return False
            
        
        for i in range(M):
            for j in range(N):
                if dfs(i,j, 0):
                    return True
        return False