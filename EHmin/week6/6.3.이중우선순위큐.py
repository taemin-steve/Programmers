from heapq import *

def solution(operations):
    #max heap인지 확인하는 flag
    is_max = False
    heap = []
    answer = [0,0]
    
    for operation in operations:
        operator, value = operation.split()
        #명령어가 I인 경우 
        if operator == 'I':
            if is_max:
                heappush(heap,-int(value)) # max heap인 경우 -1을 곱한 값을 heappush 
            else:
                heappush(heap,int(value))
        #명령어가 D인 경우 
        elif operator == 'D':
            if not heap:
                continue
            #최댓값 pop
            if value == '1':
                if is_max:
                    heapify(heap)
                    heappop(heap)
                else: #min heap 힙인경우 
                    heap = [ -1 * i for i in heap] # 모두 -1 곱해서 재정렬
                    heapify(heap)
                    is_max = True
                    heappop(heap)
            #최솟값 pop
            elif value == '-1':
                if is_max: #max heap인경우
                    heap = [ -1 * i for i in heap]
                    heapify(heap)
                    is_max = False
                    heappop(heap)
                else:
                    heappop(heap)
                    
    # heap이 비어있지 않은경우             
    if heap:
        answer.clear()
        #최대 최솟값을 answer로 지정
        if is_max:
            heap = [ -1 * i for i in heap]
            heap = sorted(heap)
        else:
            heap = sorted(heap)
        answer = [heap[-1], heap[0]]

    return answer
        

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))