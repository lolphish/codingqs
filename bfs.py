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
# beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] only change 1 letter at time (bidirect BFS)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0
        front, back, length = set(), set(), 2
        front.add(beginWord)
        back.add(endWord)
        wordDict = set(wordList)
        wordDict.discard(beginWord) # remove front word
        while front:
            posWords =  set([word[:i] + char + word[i+1:] for word in front for i in range(len(beginWord)) for char in string.ascii_lowercase]) # generate all words
            front = posWords & wordDict # check if the posWords are in wordList by set intersection
            if front & back:
                return length # if there's any intersection there's a match
            length += 1
            if len(front) > len(back):
                front, back = back,front # switch to the other side of bfs if smaller and repeat
            wordDict -= front # to remove cycles
            
        return 0
        

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

# zig zag traversal: print each level from left->right, then right->left alternatingly. Sol: use a flag
def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    queue, res, flag = deque(), deque(), False
    queue.append(root)
    while queue:
        next = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if flag:
                next.insert(0, node.val)
            else:
                next.append(node.val)
    
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        res.append(next)
        flag = not flag
    return list(res)


def tiltMaze(maze, sx, sy, dx, dy):
    M, N = len(maze), len(maze[0])
    visited = [[False]*N for _ in range(M)]
    queue = deque()
    queue.appendleft((sx, sy))
    directions = [(-1, 0), (1,0), (0,-1), (0,1)]
    depth = 0
    while queue:
        point = queue.pop()
        
        if point[0] == dx and point[1] == dy:
            return depth
        depth+=1
        for d in directions:
            new_point = (point[0]+d[0], point[1]+d[1])
            if not (0 <= new_point[0] < M and 0 <= new_point[1] < N) or maze[new_point[0]][new_point[1]] == 1 or visited[new_point[0]][new_point[1]]:
                continue
                
            while 0 <= new_point[0]+d[0] < M and 0 <= new_point[1]+d[1] < N and maze[new_point[0]+d[0]][new_point[1]+d[1]] == 0:
                new_point = (new_point[0]+d[0], new_point[1]+d[1])
            
            if not visited[new_point[0]][new_point[1]]:
                visited[new_point[0]][new_point[1]] = True
                queue.appendleft(new_point)
    return -1
    

maze = [ [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0]]
print(tiltMaze(maze, 0, 4, 4, 4))