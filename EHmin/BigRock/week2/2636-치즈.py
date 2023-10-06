# 사각형 모양의 판 회색 >> 치즈가 있다. 가장자리에는 치즈 없고 치즈에는 구명이 있을수 있음
# 구멍에는 원래 안녹는데, 겉에는 녹을 수 있음 
# 녹는데 까지 걸리는 시간과 직전의 치즈 조각의 수 
# 가로 세로 최대 100 
# 겉이라는걸 어떻게 알것인가? >> 상하좌우에 하나라도 없으면 겉이다
# 그럼 Fold Fill 로 하면서 진행하면 된다. 


# 입력을 받아주고 
import sys
sys.setrecursionlimit(11111)
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def DFS_OUTSIDE(y,x,m,visited):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or ny>=R or nx<0 or nx>=C: continue
        if visited[ny][nx] == 1: continue # 방문이미 했는가 
        if m[ny][nx] == 1: continue # 1인 지역은 가지 않음 
        visited[ny][nx] = 1 # 방문처리 해주고 
        m[ny][nx] = 2
        DFS_OUTSIDE(ny,nx,m,visited)
    

def DFS(y,x,m,visited):
    global count_c
    is_out = False
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or ny>=R or nx<0 or nx>=C: continue
        if visited[ny][nx] == 1: continue # 방문이미 했는가 
        if m[ny][nx] == 2 : # 바깥인지 확인 + 치즈 아니면 안감 
            is_out = True
            continue
        if m[ny][nx] == 0: continue
        visited[ny][nx] = 1 # 방문처리 해주고 
        count_c += 1
        DFS(ny,nx,m,visited)
    if is_out:
        m[y][x] = 0
    

R,C = map(int, input().split())

m = []

for _ in range(R):
    m.append(list(map(int, input().split())))
# print()
    
count = 0
final_c = 0
while True:
    count_c = 0
    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[0][0] = 1
    m[0][0] = 2
    DFS_OUTSIDE(0,0,m,visited)
    visited = [[0 for _ in range(C)] for _ in range(R)]
    
    for y in range(R):
        for x in range(C):
            if m[y][x] == 1:
                if visited[y][x] == 1 : continue
                visited[y][x] = 1
                count_c += 1
                DFS(y,x,m,visited)
                
    # if count < 3:
    #     for l in m:
    #         print(*l)
    #     print()
    
    if count_c == 0:
        break
    
    final_c = count_c
    count += 1
    
print(count)
print(final_c)
            
# 이렇게 DFS를 두번 돌리지 않고, 다음과 같은 접근 방식도 가능함 
# 0 인부분 전부 돌면서, 1인부분 만나면 배열에 저장 
# 이후 배열에 있는 부분들을 0으로 변환 
# 배열에 들어있던 것중, 마지막에 끝나기 직전의 개수가 직전의 개수임!