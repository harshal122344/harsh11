from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

print("BFS Traversal:")
bfs('A')