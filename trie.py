'''
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Output: ["eat","oath"]
'''
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
    #make trie
        trie={}
        for w in words:
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'
        self.res=set()
        self.used=[[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,'')
        return list(self.res)
    
    def find(self,board,i,j,trie,pre):
        if '#' in trie:
            self.res.add(pre)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j]=True
            self.find(board,i+1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j+1,trie[board[i][j]],pre+board[i][j])
            self.find(board,i-1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j-1,trie[board[i][j]],pre+board[i][j])
            self.used[i][j]=False


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.is_word = False