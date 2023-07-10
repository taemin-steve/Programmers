from collections import deque
def solution(bridge_length, weight, truck_weights):
    lifted_truck = deque([0 for i in range(bridge_length)])
    truck_queue = deque(truck_weights)
    lifted_weight = 0
    count = 0
    while True:
        lifted_weight -= lifted_truck.popleft()
        if lifted_weight + truck_queue[0] <= weight:
            temp = truck_queue.popleft()
            lifted_weight += temp
            lifted_truck.append(temp)
        else:
            lifted_truck.append(0)
        count += 1
        if not truck_queue:
            return count + bridge_length 
        print(lifted_weight)
        
# def solution(bridge_length, weight, truck_weights):
    
#     lifted_truck = deque([0 for i in range(bridge_length)])
#     truck_queue = deque(truck_weights)
#     count = 0
#     while True:
#         lifted_truck.popleft()
#         if sum(lifted_truck) + truck_queue[0] <= weight:
#             lifted_truck.append(truck_queue.popleft())
#         else:
#             lifted_truck.append(0)
#         count += 1
#         if not truck_queue:
#             return count + bridge_length 
#         print(sum(lifted_truck))
            

#------------------------------------------------------------
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]	
print(solution(bridge_length, weight, truck_weights))