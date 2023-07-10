from collections import deque
def solution(prices):
    answer = []
    dq = deque(prices)
    #주식 가격이 내려가지 않는 time
    sec=0
    #큐가 빌때까지 반복
    while(dq):
        #앞에서 하나씩 빼서 기준으로 설정
        flag = dq.popleft()
        #큐에 남은 원소들을 반복문으로 돌면서 flag 비교
        for i in dq:
            sec=sec+1 #다른 원소랑 비교하는 시점에 이미 1초가 지났음
            if(i<flag):
                break
        answer.append(sec)
        sec = 0
    return answer
                
    
