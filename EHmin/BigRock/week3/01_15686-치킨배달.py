# N x N 인 도시  빈칸 / 치킨집/ 집 셋중ㅇ하나 
# r, c는 1부터 시작함 
# 치킨 거리 == 집과 가장 가까운 치킨집의거리 
# 도시의 치킨 거리는 각각의 집에서 치킨 거리의 합 
# 치킨 집의 개수는 최대 M 개 
# 어떻게 고르면 , 치킨거리를 최소로 만들어줄 수 있는가 

# 집의 개수 최대 100 개 // 치킨집의 개수는 최대 13 이러면 각각의 집에서 bfs 하면서 100 개에 대해서 bfs 
# 13C6 1000000 * 100 bfs(??)
# 13C6 100000 * 100 * bfs 100 10번인데... 근데 이거 말고 딱히 없을거같아 
# 100000 * (100 * 치킨집 최대 13개 아님?) 

# 1 == 집 2== 치킨
from itertools import combinations

N, M = map(int, input().split())
adj = []
c_list = [] # 치킨집 리스트 
h_list = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            c_list.append([i,j])
        elif temp[j] == 1:
            h_list.append([i,j])
    adj.append(c_list)

ans = 1000000 # 진짜 최소 

for rc in combinations(c_list, M): 
    #각각의 집에서 치킨집 중 제일 가까운거 구하기 
    temp_sum = 0
    for house in h_list: # 모든 집에대해서 수행 
        house_min = 10000 # 집에서 가장 가까운 치킨집 까지의 거리 
        for chec in rc:
            temp = abs(chec[0] - house[0]) + abs(chec[1] - house[1])
            house_min = min(temp, house_min)
        temp_sum += house_min
    ans = min(temp_sum, ans)
    
print(ans)

