from collections import deque, defaultdict

def solution(program): 
    # 프로그램 정렬 우선순위는 시간으로
    program.sort(key = lambda x: (x[1],x[0])) # 가장 빠르고, 우선순위 높은게 제일 먼저 있음! 
    
    c_time  = 0
    
    q = deque(program)
    temp = [q.popleft()]
    d = defaultdict(int)
    
    while True:
        # 프로그램 실행
        if not q and not temp:
            break
        if temp:
            importance, time_in, time_use = temp.pop()
            print(importance, time_in, time_use)
            c_time = max(c_time,time_in)
            d[importance] += (c_time - time_in)
            c_time += time_use
            print(d)
        
        # queue에 올려주는작업 
        while q and c_time >= q[0][1]:
            temp.append(q.popleft())
         
        if q and not temp:
            temp.append(q.popleft())
        temp.sort(key = lambda x: (-x[0],-x[1]))
        
    answer = [0 for _ in range(10)]
    
    for k in d.keys():
        answer[k-1] = d[k]
        
    return [c_time] + answer


print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))

#우선순위 큐가 있다. 이걸로 해야할듯??