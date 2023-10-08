# 지훈이가 불에 타기 전에, 얼마나 빨리 탈출할 수 있는지 결정하기
# 불ㅇㄴ 상하좌우로 타고 들어간다 
#  벽게 붙으면 탈출 가능 
# R, C > 1000
# #> 벽 . 지나갈수 있음 J 초기위치 / F 불공간 
# 불을 먼저 업데이트 시키자. # 탈출 조건도 명시 

# DFS 
# 초기조건 확인하고 
# 불을 확장할 칸 임시저장 
# DFS
# 확장한칸 삭제

# 입력을 받아주고 
from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def fire(y,x):
    global adj, visited_f 
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or ny>=R or nx<0 or nx>=C : continue
        if visited_f[ny][nx] : continue
        if adj[ny][nx] == 'F' or adj[ny][nx] == '#' : continue
        visited_f[ny][nx] = True
        adj[ny][nx] = 'F'
        
def go(y,x):
    global adj, visited
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or ny>=R or nx<0 or nx>=C : continue
        if visited[ny][nx] : continue
        if adj[ny][nx] == 'F' or adj[ny][nx] == '#' : continue
        visited[ny][nx] = True
        adj[ny][nx] = 'J'
        if ny==0 or ny==R-1 or nx==0 or nx==C-1: return True
        
        
R, C = map(int, input().split())
adj = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
visited_f = [[False for _ in range(C)] for _ in range(R)]

q = deque([])

for i in range(R):
    for j in range(C):
        if adj[i][j] == 'J':
            q.append([i,j])

count = 0
fin = False
impossible = True

while True:
    impossible = True
    count += 1
    
    # 지훈을 먼저 업데이트 해주고 
    visited = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if adj[i][j] == 'J':
                if visited[i][j] : continue
                visited[i][j] = True
                impossible = False
                if go(i,j): 
                    fin = True
                    break
    # print()
    # for k in adj:
    #     print(*k)
                
    if impossible : break
    if fin: break
                
    # 불 업데이트 
    for i in range(R):
        for j in range(C):
            if adj[i][j] == 'F':
                if visited_f[i][j] : continue
                visited_f[i][j] = True 
                fire(i,j)
    # print()
    # for k in adj:
    #     print(*k)


if impossible : print("IMPOSSIBLE")
else : print(count + 1)
    # 00?xx
