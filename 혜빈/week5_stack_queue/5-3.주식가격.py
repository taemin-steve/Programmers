#list 사용 => 시간초과
from collections import deque
def solution(prices):
    answer =[]
    prices=deque(prices) 

    while prices: #prices 배열이 빌 때까지
        sec=0 #매 요소마다 시간 초기화
        price=prices.popleft() #가장 앞의 주식가격
        for p in prices: #주식 가격만큼
            sec+=1 #1초씩 경과
            if price>p: #가격이 내려가면
                break #더 이상 시간을 더하지 않고 탈출
        answer.append(sec) #answer에 각 주식 가격이 안 떨어진 시간 추가

    return answer

solution([1, 2, 3, 2, 3]) #[4, 3, 1, 1, 0]