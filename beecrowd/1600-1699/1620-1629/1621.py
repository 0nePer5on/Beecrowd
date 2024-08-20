from collections import deque

graph = {
  'S' : ['A','B', 'C'],
  'A' : ['D'],
  'B' : ['E'],
  'C' : ['F', 'J'],
  'D' : ['G'],
  'E' : ['I', 'J'],
  'F' : ['S'],
  'G' : ['H'],
  'I' : [],
  'J' : [],
  'H' : ['D']
}

def bfs(graph, node, target):
    # These lists should not be global. At each call of BFS, they should reset
    visited = {}  # Use a dict so you can store where the visit came from
    queue = deque()    # Use a deque to not lose efficiency with pop(0)

    visited[node] = None
    queue.append(node)
    
    while queue:
        m = queue.popleft() 
        if m == target:  # Bingo!
            # Extract path from visited information
            path = []
            while m:
                path.append(m)
                m = visited[m]  # Walk back
            return path[::-1]  # Reverse it
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited[neighbour] = m  # Remember where we came from
                queue.append(neighbour)
                
# Driver Code
print("Following is the Breadth-First Search")
print(bfs(graph, 'S', 'H'))