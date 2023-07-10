from heapq import *

def solution(scoville, K):
    heap = scoville
    heapify(heap)
    count = 0
    while (heap[0] < K):
        # 조건을 만족시키지 못하는 경우 > -1 return 
        if len(heap) == 1:
            return -1
        #두 개를 섞고 저장 
        smallest = heappop(heap)
        smallest += heappop(heap) * 2 
        heappush(heap, smallest)
        count += 1
    return count


scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))
