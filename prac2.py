from collections import deque
graph ={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
def bfs (start):
    visited=set()
    queue=deque()

    visited.add(start)
    queue.append(start)
    while queue:

        vertex = queue.popleft()

        print(vertex, end=" ")

        for neighbor in graph[vertex]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Function call should be outside the function
print("Breadth First Search Traversal:")
bfs('A')