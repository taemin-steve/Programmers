from collections import deque

def process_order(priorities, location):
    
    sorted_priorities = sorted(priorities) #오름차순 정렬
    target_process_prior = priorities[location] #출력하고 싶은 프로세스 우선순위
    
    list_for_queue = priorities
    list_for_queue[location] = -1 # index 정보를 기억하지 않을 것이기에 겹치지 않는 정수인 -1로 저장 
    
    queue = deque(list_for_queue)
    count = 0
    while True:
        temp = queue.popleft()
        # 출력하고 싶은 process인 경우 
        if temp == -1:
            if sorted_priorities[-1] == target_process_prior: #현재 출력할 차례인 경우 
                return count + 1
        # 일반 process인경우 
        if temp == sorted_priorities[-1]: #최고 우선순위 프로세스인경우 
            count += 1 #시행된 프로세스 수 갱신 
            sorted_priorities.pop() #최고 우선순위 갱신 
        else:
            queue.append(temp)
        print(queue)
        

priorities = [2, 1, 3, 2]
location = 2

print(process_order(priorities, location))