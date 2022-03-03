import sys
from collections import deque

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
graph = []
n, m = map(int, sys.stdin.readline().split())

for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[-1 for col in range(n)] for row in range(m)]
dq = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dq.append((i, j))
            visited[i][j] = 0
        elif graph[i][j] == -1:
            visited[i][j] = -2

while dq:
    parent = dq.popleft()
    for i in range(4):
        child_x, child_y = parent[0]+dx[i], parent[1]+dy[i]
        if child_x < 0 or child_y < 0:
            continue
        if child_x >= m or child_y >= n:
            continue
        if visited[child_x][child_y] == -1 and graph[child_x][child_y] == 0:
            visited[child_x][child_y] = visited[parent[0]][parent[1]] + 1
            dq.append((child_x, child_y))

answer = -2
flag = False
for v in visited:
    for idx in v:
        if idx > answer:
            answer = idx
        if idx==-1:
            answer = idx
            flag = True
            break
    if flag: break
print(answer)
