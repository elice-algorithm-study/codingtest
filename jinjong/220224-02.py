from collections import deque

def bfs(node, graph, visited):
    dq = deque()
    dq.append(node)
    while dq:
        parent = dq.popleft()
        for child in graph[parent]:
            if visited[child] == -1:
                visited[child] = visited[parent] + 1
                dq.append(child)

def solution(n, edge):
    answer = 0
    graph = dict()
    visited = [-1 for i in range(n+1)]
    visited[1] = 0
    
    for i in range(1, n+1):
        graph[i] = []
        
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    bfs(1, graph, visited)
    
    maxNum = max(visited)
    for v in visited:
        if v == maxNum:
            answer+=1
    
    return answer
