import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().split())
order = 1

def dfs(node):
    global order
    visited[node] = order

    for i in graph[node]:
        if visited[i] == 0:
            order += 1
            dfs(i)
    return

if __name__ == "__main__":
    graph = dict()
    visited = [0 for i in range(n+1)]
    
    for i in range(n):
        graph[i+1] = list()
    
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for key, value in graph.items():
        value.sort(reverse=True)

    dfs(r)
    
    for i in range(1, n+1):
        print(visited[i])
