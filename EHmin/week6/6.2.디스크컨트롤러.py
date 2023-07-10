from heapq import *

def solution(jobs):
    #2차원 배열을 tuple의 형태로 저장 > 튜플의 첫번째 원소를 기준으로 heap 정렬 진행
    input_jobs = [tuple(job) for job in jobs]  
    heapify(input_jobs)
    
    # 현재 시간
    current_time = input_jobs[0][0] 
    
    # 다음에 실행 가능한 job
    next_candidate = [] 
    heapify(next_candidate)
    
    #next candidate이 비어있는지 확인
    nothing_todo = True

    #해당 작업이 수행하는 동안 대기한 시간
    time_cost = []
    
    while input_jobs or next_candidate :
        # current_time 기준으로 next_candidate에 heappush
        while input_jobs and (input_jobs[0][0] <= current_time):
            item = heappop(input_jobs)
            heappush(next_candidate, (item[1], item[0])) # 튜플의 순서 변환
            nothing_todo = False
        
        # next_candidate이 비어있는 경우 current_time을 다음 실행 가능한 시점으로 변경
        if nothing_todo:
            current_time = input_jobs[0][0]
        else:
            #next_candidate에 존재하는 가장 작은값 리턴
            item = heappop(next_candidate) 
            current_time += item[0]
            time_cost.append(current_time - item[1]) #소요된 시간 계산
            # next_candidate이 비어있는 경우 flag 전환
            if not next_candidate:
                nothing_todo = True
        
    return int(sum(time_cost)/len(time_cost))

jobs = [[0, 10], [0, 1], [0, 1]]

print(solution(jobs))