# 길이 H, 가로 W인 직사각형 모양 
# 기본행렬과 동일 
# 모든 구름은 1분마다 오른쪽으로 한칸씩 이동한다. , 외부에서 들어오는건 없음 
# 각 구역에 대해 몇분후에 처음! 구름이 오는지 

H, W = map(int,input().split())
M = [list(input()) for _ in range(H)]
C_M = [[-1 for _ in range(W)] for _ in range(H)]

def DFS(y, x ,M ,C_M):
    if x + 1 < W and M[y][x+1] != "c":
        C_M[y][x+1] = C_M[y][x] + 1
        DFS(y, x+1, M, C_M)
    
    
# 모든 C에 대해서 진행 
for i in range(H):
    for j in range(W):
        if M[i][j] == 'c':
            C_M[i][j] = 0 
            DFS(i,j,M,C_M)

for i in C_M:
    print(" ".join(map(str,i)))
    