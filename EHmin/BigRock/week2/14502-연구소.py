# 바이러스가 2, 1은 벽임
# 벽을 3개 더 칠수 있고, 바이러스는 벽안치면 상하자우로 감 
# 벽 꼭 3개 더쳤을때, 퍼저나갈 수 있는 최대크기를 구해줘 
# 그냥 가능한거 다 치자 어때 

# 안전영역을 어떻게 찾아주는지가 문제인데... 

from itertools import combinations
import copy

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def DFS(y,x,m,visited):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny<0 or ny>=N or nx<0 or nx>=M: continue
        if visited[ny][nx] == 1: continue
        if m[ny][nx] == 1: continue
        
        visited[ny][nx] = 1
        global count
        count += 1
        DFS(ny,nx,m,visited)
        

N, M = map(int, input().split())
space_0 = []

m = []
ans = 0
wall = 0

for i in range(N):
    s = list(map(int,input().split()))
    for j in range(len(s)):
        if s[j] == 0:
            space_0.append([i,j])
        if s[j] == 1:
            wall += 1
    m.append(s)
    
p_c = True
    
for first, second, third in  combinations(range(len(space_0)),3):
    m[space_0[first][0]][space_0[first][1]] = 1
    m[space_0[second][0]][space_0[second][1]] = 1
    m[space_0[third][0]][space_0[third][1]] = 1
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 2: ## 바이러스 먼저 Fooldfill 해주자
                if visited[i][j] == 1: continue
                visited[i][j] = 1
                count += 1
                DFS(i,j, m,visited)
    ans = max(ans, N*M - wall -3 - count)
    m[space_0[first][0]][space_0[first][1]] = 0
    m[space_0[second][0]][space_0[second][1]] = 0
    m[space_0[third][0]][space_0[third][1]] = 0
    
print(ans)