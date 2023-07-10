import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    if(scoville[0]>=K): # 처음부터 min이 임계치 넘어가면 더 이상 돌 필요 없음
            return answer
    
    #조건 만족이 안되는 애들, 조건 맞춰주기
    while(len(scoville)>=2): #길이가 1개가 되어버리면 인덱스 에러   
        minScov1 = heapq.heappop(scoville)
        minScov2 = heapq.heappop(scoville)
        newScov = minScov1 + 2 * minScov2
        heapq.heappush(scoville, newScov)
        answer = answer + 1
        if(scoville[0]>=K):
            return answer
        
    #길이 1될때까지 조건 못맞추면 그냥 -1 반환    
    return -1 
    
print(solution([1, 2, 3, 9, 10, 12], 7))