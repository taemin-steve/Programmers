# # 컴퓨터 N 대 
# # 서로 신뢰한느 관계// A >> B 라면 B해킹시 A 도 자동해킹 뭐 해킹하면 가장 효율적이야?
# # 그럼 Root node를 찾아주는게 제일 좋은데, 모두 다 돌수는 없어 효율적으로 접근하는 방식을 찾아야해 
# # 결국 Root Node라는 것은 신뢰하는 것이 없는 친구 
# # 그런데 신뢰하는게 모두 없다면?? ㅁ도ㅜ 따리 따리 한다면 ?? 상과 없음 

# # DFS 탐색 
# import sys

# sys.setrecursionlimit(1000)

# def DFS(start,m, visited):
#     global temp 
#     for node in m[start]:
#         if visited[node] == True: continue
#         temp += 1
#         visited[node] = True
#         DFS(node,m, visited)
        
# # 입력 받기 
# N,M = map(int, input().split())

# # 신뢰 리스트 생성 t_l 
# t_l = [[] for _ in range(N)]
# # is_root = [True for _ in range(N)]

# # 연결 리스트 생성 , 신뢰 리스트에 같이 저장 해주기 
# for _ in range(M):
#     a, b = map(int, input().split())
#     # is_root[a-1] = False # a는 1부터 들어오기 때문에 -1 처리 
#     t_l[b-1].append(a-1) # 신뢰 받는 방향으로 뻗을 수 있게 링크 생성

# # 신뢰 리스트 순회하면서 DFS, Count Global로 만들어서 진행 
# count = 0
# candidate = [0]
# for i in range(N):
#     # if not is_root[i]: continue
#     visited = [False for _ in range(N)]
#     temp = 1
#     visited[i] = True
#     DFS(i,t_l, visited)
#     if count > temp: continue
#     elif count < temp :
#         candidate.clear()
#         candidate.append(i+1)
#     elif count == temp:
#         candidate.append(i+1)
#     count = max(count, temp)
#     visited.clear()
#     # print(temp)
#     # print(candidate)

    
# # ans = []

# # for item in candidate:
# #     if item[1] == count:
# #         ans.append(item[0])

# candidate.sort()
# print(*candidate)
# BFS로 풀어야함 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ


# 입력 받기 
from collections import deque

N,M = map(int, input().split())

# 신뢰 리스트 생성 t_l 
t_l = [[] for _ in range(N)]
# is_root = [True for _ in range(N)]

# 연결 리스트 생성 , 신뢰 리스트에 같이 저장 해주기 
for _ in range(M):
    a, b = map(int, input().split())
    t_l[b-1].append(a-1) # 신뢰 받는 방향으로 뻗을 수 있게 링크 생성
    
count = 0
candidate = [0]

for i in range(N):
    q = deque([])
    visited = [False for _ in range(N)]
    temp = 1
    
    #bfs
    q.append(i)
    visited[i] = True
    
    while q:
        node = q.popleft()
        for nnode in t_l[node]:
            if visited[nnode] : continue
            visited[nnode] = True
            q.append(nnode)
            temp += 1
            
    if count > temp: continue
    elif count < temp :
        candidate.clear()
        candidate.append(i+1)
    elif count == temp:
        candidate.append(i+1)
    count = max(count, temp)   

candidate.sort()
print(*candidate)