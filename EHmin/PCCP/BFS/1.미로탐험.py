#입력과 출력을 자유롭게 작성해주세요
from collections import deque

H , W = map(int, input().split())

graph = [list(map(int, input()))for _ in range(H)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

q = deque([])

def bfs( graph, row, col):
    q.append([row,col])
    
    while q:
        item = q.popleft()
        for i in range(4):
            new_r = item[0] + dr[i]
            new_c = item[1] + dc[i]
            
            if new_r >= 0 and new_r < H and new_c >=0 and new_c < W:
                if graph[new_r][new_c] == -1:
                    graph[new_r][new_c] = graph[item[0]][item[1]] + 1
                    q.append([new_r, new_c])

start_pos = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 1:
            graph[i][j] = -1
        elif graph[i][j] == 2:
            start_pos = [i,j]
            graph[i][j] = 0

bfs(graph , start_pos[0], start_pos[1])
                    
for rows in graph:
    print(" ".join(map(str, rows)))