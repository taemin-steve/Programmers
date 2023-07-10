import heapq
def solution(operations):
    answer = []
    que = []
    for operation in operations:
        x, num = operation.split() 
        num = int(num)
        
        if x == 'I':
            heapq.heappush(que, num)
        elif x == 'D' and num == 1:
            if len(que) != 0:
                max_value = max(que)
                que.remove(max_value)
        else:
            if len(que) != 0:
                heapq.heappop(que)
    
    if len(que) == 0:
        answer = [0, 0]
    else:
        answer = [max(que), heapq.heappop(que)]
        
    return answer