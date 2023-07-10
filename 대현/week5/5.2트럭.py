from collections import deque
def solution(bridge_length, weight, truck_weights):
    #진짜 트럭들이 다리를 건너는 것처럼 deque 구현
    lifted_truck = deque([0]*bridge_length)
    truck_queue = deque(truck_weights)
    lifted_weight = 0
    count = 0
    while True:
        #단순히 sum함수 쓰면 시간복잡도 걸림
        lifted_weight = lifted_weight - lifted_truck.popleft()
        if lifted_weight + truck_queue[0] <= weight:
            temp = truck_queue.popleft()
            lifted_weight = lifted_weight + temp
            lifted_truck.append(temp)
        else:
            lifted_truck.append(0)
        count = count + 1
        if not truck_queue:
            return count + bridge_length 
        # print(lifted_weight)
