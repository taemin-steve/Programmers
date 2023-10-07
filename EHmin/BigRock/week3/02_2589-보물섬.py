# L - 육지 W- 바다 
# 한칸 이동에 한시간 >> BFS 
# 보물은 육지 기준 가장 떨어진 곳에 서로 위치한다.
# 전체 탐색이 가능한가 ?? >> 모든 노드에 대해서 진행 
# 2500 * 2500 >> 10000000 돌아볼만함 

from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 입력 받아주고 
R, C = map(int, input().split())
adj = [list(input()) for _ in range(R)] # 지도 
ans = 0
# visited = [[False for _ in range(C)] for _ in range(R)]
q = deque([])
# L 인 모든 노드에 대해서 BFS
for i in range(R):
    for j in range(C):
        visited = [[0 for _ in range(C)] for _ in range(R)] # 매번 초기화
        temp = 0
        if adj[i][j] == 'L' and visited[i][j] == 0:
            visited[i][j] = 1
            q.append([i,j])
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny<0 or ny>=R or nx<0 or nx>=C: continue
                    if adj[ny][nx] == "W" : continue
                    if visited[ny][nx] != 0: continue
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny,nx])
                    temp = max(visited[ny][nx], temp)
                    # for t in visited:
                    #     print(*t)
                    # print()
            # print(temp)
        ans = max(temp,ans)

print(ans - 1)
# DFS 하면서 최대의 최단거리를 저장 