import numpy as np
from collections import deque

def solution(prices):
    # answer = []
    # for i in range(len(prices)):
    #     count = 0
    #     for j in prices[i+1:]:
    #         count += 1
    #         if j < prices[i]:
    #             break
    #     answer.append(count)
    
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer
        

prices =[1, 2, 3, 2, 3]

print(solution(prices))
    # for i in range(len(prices)):
    #     count = 0
    #     for j in prices[i+1:]:
    #         count += 1
    #         if j < prices[i]:
    #             break
    #     answer.append(count)
        
    # return answer