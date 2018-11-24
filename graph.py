from collections import defaultdict,deque
from edge import edge
def addEdge(graph, from_node:int, to_node:int, cost:int):
    graph[from_node].append(edge( from_node, to_node, cost))

# Topological Sorting
#Use a stack. For each vertices, recursively call function to visit all neighbors and add to stack when we run out of vertices to visit. Then at the end pop from the stack.
 def topologicalSortUtil(self,v,visited,stack):
        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
        # Push current vertex to stack which stores result
        stack.insert(0,v)
 def topologicalSort(self):
    for i in V: if visited[i] == False: topologicalSortUtil(i,visited,stack)

# topological sorting
def topSort(graph:defaultdict):
    visited = set() # add visited node into here
    res = deque()
    for i in graph.keys():
        if i not in visited:
            topSortUtil(graph, i, visited, res)
    return res

def topSortUtil(graph, node, visited:set, stack:deque):
    visited.add(node)
    if node not in graph:
        stack.append(node)
        return
    for adj in graph[node]:
        if adj.to_node not in visited:
            topSortUtil(graph, adj.to_node, visited, stack)
    stack.append(node)

# Shortest path
def shortestPath(graph, from_node, to_node):
    st = topSort(graph)
    print(st)
    dist = {n:float("inf") for n in st}
    dist[from_node] = 0
    while st:
        n = st.pop()
        print(n)
        for i in graph[n]:
            if dist[n]+ i.cost < dist[i.to_node]:
                dist[i.to_node] = dist[n] + i.cost
    return dist

# longest path
def longestPath(graph, from_node, to_node):
    st = topSort(graph)
    dist = {n:float("-inf") for n in st}
    dist[from_node] = 0
    while st:
        n = st.pop()
        for i in graph[n]:
            if dist[n]+ i.cost > dist[i.to_node]:
                dist[i.to_node] = dist[n] + i.cost
    return dist


# cycle detection
def detectCycle(graph, node):
    visited = set()
    for i in graph.keys():
        if i not in visited:
            if cycleUtil(graph, i, visited, set()):
                return True
    return False

def cycleUtil(graph, node, visited, rec):
    visited.add(node)
    rec.add(node)
    for adj in graph[node]:
        if adj.to_node not in visited:
            if cycleUtil(graph, adj.to_node, visited, rec):
                return True
        elif adj in rec:
            return True
    rec.remove(node)
    return False


def maxVacationDays(self, flights, days):
    NINF = float('-inf')
    N, K = len(days), len(days[0])
    best = [NINF] * N
    best[0] = 0

    for t in range(K):
        cur = [NINF] * N
        for i in range(N):
            for j, adj in enumerate(flights[i]):
                if adj or i == j:
                    cur[j] = max(cur[j], best[i] + days[j][t])
        best = cur
    return max(best)


if __name__ == "__main__":
    numNodes = 8
    graph = defaultdict(list)
    addEdge(graph, "A", "B", 3)
    addEdge(graph, "A", "C", 6)
    addEdge(graph, "B", "C", 4)
    addEdge(graph, "B", "D", 4)
    addEdge(graph, "B", "E", 11)
    addEdge(graph, "C", "D", 8)
    addEdge(graph, "C", "G", 11)
    addEdge(graph, "D", "E", -4)
    addEdge(graph, "D", "F", 5)
    addEdge(graph, "D", "G", 2)
    addEdge(graph, "E", "H", 9)
    addEdge(graph, "F", "H", 1)
    addEdge(graph, "G", "H", 2)
    print(shortestPath(graph,"A","G"))
    print(longestPath(graph,"A","G"))
