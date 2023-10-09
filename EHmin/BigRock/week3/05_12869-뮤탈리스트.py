# 수빈이는 뮤탈 한개 강호는 S 하나 남음
# SCV는 체력있고, 뮤탈 공격못함. 
# 뮤탈은 공겨할때 한번에 3개의 SCV 공격가능함
# SCV 체력이 0 혹은 이하가 되면 파괴됨. 
# 첫번째 공격은 9 그담 3 그담 1임 
# 1. 누구를 먼저 때리는지가 문제임. 
# 2. 그담에 먼저 터졌을때, 어떻게 될지가 문제임 >> 리스트에 담아놨다가, 터지면 pop 해주는게 어때? 
# 12 > 어차피 얘가 먼저 터저야함 
# 45 20 5 매번 가장 큰 친구 패주자 

n = int(input())
scv = list(map(int, input().split()))
dp = [[[61] * 61 for _ in range(61)] for _ in range(61)] 
hits = 61 

while len(scv)!= 3:
    scv.append(0)
    
def mutal(x,y,z):
    global hits
    x,y,z
    if x <= 0 and y <= 0 and z <= 0:
        hits = min(hits, dp[x][y][z])
        return
    for i in ((9, 3, 1), (9, 1, 3), (3, 1, 9), (3, 9, 1), (1, 9, 3), (1, 3, 9)):
        nx = x - i[0]
        ny = y - i[1]
        nz = z - i[2]
        if nx < 0:
            nx = 0
        if ny < 0:
            ny = 0
        if nz < 0:
            nz = 0
        if dp[nx][ny][nz] > dp[x][y][z] + 1:
            dp[nx][ny][nz] = dp[x][y][z] + 1
            mutal(nx, ny, nz)
    
dp[scv[0]][scv[1]][scv[2]] = 0
mutal(scv[0], scv[1], scv[2])
print(hits)

## 추후에 다시 풀어보자!