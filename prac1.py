graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}   
visited=set()
def dfs(vertex):
    if vertex not in visited:
        print(vertex,end=' ')
        visited.add(vertex)
        for neighbour in graph[vertex]:
            dfs(neighbour)

print("Depth First Search Traversal:")
dfs('A')