from collections import deque
from unionfind import unionfind
# dp and matrix problems
def knapsack(values:int, weight: int, W:int):
    dp = [[0] * (W+1) for _ in len(values)+1]
    for i in range(values):
        for w in range(W):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i-1] > w: # if item's weight is higher than w
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(values[i-1][w-weight[i-1]], dp[i-1][w])
    return dp[len(values)][W]


def shortestDistanceFromAllBuildings(grid):
    '''
     hit = # of times a grid has been reached
     distSum = sum of distances from all 1 grid to 0 grid

    '''
    if not grid or not grid[0]: return -1
    M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
    hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]

    def bfs(start_x, start_y):
        visited = [[False] * N for k in range(M)]
        visited[start_x][start_y], count1, queue = True, 1, deque([(start_x, start_y, 0)])
        # count 1 used for pruning
        while queue:
            x,y,dist = queue.popleft()
            for i, j in ( (x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                    visited[i][j] = True
                    if grid[i][j] == 0: # if not grid[i][j] works too
                        queue.append((i,j,dist+1))
                        hit[i][j] +=1
                        distSum[i][j] += dist + 1
                    elif grid[i][j] == 1:
                        count1+=1
            return count1 == buildings

    for x in range(M):
        for y in range(N):
            if grid[x][y] == 1:
                if not bfs(x,y): return -1

    return min([distSum[i][j] for i in range(M) for j in range(N) if grid[i][j] == 0 and hit[i][j] == buildings] or [-1])


def bombEnemy(grid):
    maxSum, res = [[0]*len(grid[0]) for _ in range(len(grid))], 0
    for i in range(len(grid)):
        enemies = 0
        for j in range(len(grid[0])):
            if not grid[i][j]:
                maxSum[i][j] += enemies
                res = max(maxSum[i][j], res)
            elif grid[i][j] == "E": enemies+=1
            else: enemies = 0
        enemies = 0
        for j in range(len(grid[0])-1, -1, -1):
            if not grid[i][j]:
                maxSum[i][j] += enemies
                res = max(maxSum[i][j], res)
            elif grid[i][j] == "E": enemies+=1
            else: enemies = 0
    for j in range(len(grid[0])):
        enemies = 0
        for i in range(len(grid)):
            if not grid[i][j]:
                maxSum[i][j] += enemies
                res = max(maxSum[i][j], res)
            elif grid[i][j] == "E": enemies+=1
            else: enemies = 0
        enemies = 0
        for i in range(len(grid)):
            if not grid[i][j]:
                maxSum[i][j] += enemies
                res = max(maxSum[i][j], res)
            elif grid[i][j] == "E": enemies+=1
            else: enemies = 0
    return res

def longestPathInMatrix(grid):
    if not grid or not grid[0]:
        return 0
    M,N = len(grid), len(grid[0])
    dp = [[0]*len(grid[0]) for _ in range(len(grid))]
    def dfs(i,j):
        if not dp[i][j]:
            val = grid[i][j]
            dp[i][j] = 1 + max(
                dfs(i-1,j) if i > 0 and val < grid[i-1][j] else 0,
                dfs(i+1,j) if i < M - 1 and val < grid[i+i][j] else 0,
                dfs(i, j-1) if j > 0 and val < grid[i][j-1] else 0,
                dfs(i,j+1) if  j < N - 1 and val < grid[i][j+1] else 0)
        return dp[i][j]
    return max(dfs(i,j) for i in range(M) for j in range(N))

# given a list of points that make islands, return the number of islands after each round
def numIslands2(self,n,m, positions):
    ans = []
    islands = unionfind()
    for p in map(tuple, positions):
        islands.add(p)
        for dp in (0,1),(0,-1),(1,0),(-1,0):
            q = (p[0] + dp[0], dp[1]+dp[1])
            if q in islands.parent:
                islands.union(p,q)
        ans += islands.count


'''
-1 = wall of obstacle
0 = gate
INF = empty room
find nearest gate for every room
'''
def wallsAndGates(self, rooms):
    q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
    for i, j in q:
        for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2**30:
                rooms[I][J] = rooms[i][j] + 1
                q += (I, J)


'''
The maze

'''
def hasPath(self, maze, start, destination):
    Q = [start]
    n = len(maze)
    m = len(maze[0])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while Q:
        # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
        i, j = Q.pop(0)
        maze[i][j] = 2

        if i == destination[0] and j == destination[1]:
            return True

        for x, y in dirs:
            row = i + x
            col = j + y
            while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                row += x
                col += y
            row -= x
            col -= y
            if maze[row][col] == 0:
                Q.append([row, col])

    return False


if __name__ == "__main__":
    a = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    print(shortestDistanceFromAllBuildings(a))
    b = [[0, "E", 0, 0],["E",0,"W","E"],[0,"E",0,0]]
    print(bombEnemy(b))
    c = [ [9, 9, 4], [6, 6, 8], [2, 1, 1] ]
    print(longestPathInMatrix(c))
