# N x N 크기의 땅 
# 인구이동 규칙 
# 1. 인구수 차이가 L <= x <=R 이면 국경선이 열림 
# 2. 인접한 칸을통해 이동할 수 있으면, 연합이라고 한다 
# 연합의 인구수는 총합/영토. 소수점은 버림 
# 최대경우가 5000 * 2000 대략 천만번 정도 

#입력 받아주고 
from collections import deque
import math
import sys 
sys.setrecursionlimit(2001)

dy = [-1,0,1,0]
dx = [0,1,0,-1,0]

def DFS(y,x):
    for l in range(4):
        global visited, adj, union, u_sum, temp 
        ny = y + dy[l]
        nx = x + dx[l]
        if ny<0 or ny>=N or nx<0 or nx>=N: continue
        if visited[ny][nx] : continue
        if  L <= abs(adj[y][x] - adj[ny][nx]) and abs(adj[y][x] - adj[ny][nx]) <= R :
            temp = True
            visited[ny][nx] = True
            union.append([ny,nx])
            u_sum += adj[ny][nx]
            # print()    
            # for p in visited:
            #     print(*p)
            DFS(ny,nx)
    

N, L, R = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]

count = 0
q = deque([])

for k in range(2000):
    visited = [[False for _ in range(N)] for _ in range(N)] # 회차마다 리셋 
    temp = False
    u_sum_l = []
    u_list = []
    for i in range(N): # 각각의 노드 돌면서 확인 
        for j in range(N):
            if visited[i][j] : continue
            avg = 0
            visited[i][j] = True 
            # q.append([i,j])
            union = [[i,j]]
            u_sum = adj[i][j]
            DFS(i,j)
                        
            u_sum_l.append(math.floor(u_sum/len(union)))
            u_list.append(union)
            
            # if k > 1: continue
            # print()    
            # for p in visited:
            #     print(*p)
    
    for m in range(len(u_sum_l)):
        for y, x in u_list[m]:
            adj[y][x] = u_sum_l[m]
           
    # print()    
    # for p in adj:
    #     print(*p)
    
    if temp : count += 1
    else : break
    
print(count)

