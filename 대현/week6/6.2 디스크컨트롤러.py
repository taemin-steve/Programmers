import heapq

def solution(jobs):
    time = 0 #시간을 1초씩 흘려보내기 위함
    start_time = 0
    finish_time = 0
    sum_task_time = 0 #요청부터 종료까지 걸린 시간 평균

    task_num = 0
    disk = []
    priorities = []
    waiting_tasks = []

    # for request in jobs: 
    #     heapq.heappush(priorities,request)
    heapq.heapify(jobs) #요청시간으로 heap 구성
    priorities = jobs
    task_num = len(priorities)

    while True:
        #절대시간 0초부터 시작

        #대기중인 작업 별도관리
        for t in range(len(priorities)):
            if time >= priorities[0][0]: #가장 요청 빠른거
                waiting_tasks.append(heapq.heappop(priorities))

        #대기중인 작업 작업시간이 적은 순으로 정렬
        waiting_tasks.sort(key = lambda x : x[-1])

        if disk == []:#디스크가 비어있을 때 작업을 넣기위함
            if waiting_tasks != []:
                disk = waiting_tasks.pop(0)
                start_time = time #작업이 시작된 시간을 기록
                finish_time = time + disk[1]

        elif disk != []:#디스크에 작업이 있을때 작업시간이 경과했을 때 작업 삭제
            if time == finish_time :
                sum_task_time += finish_time - disk[0]
                disk = []                

                continue

        time += 1 # 시간의 경과


        if priorities == [] and disk == []:
            break

    return int(sum_task_time/task_num)

print(solution([[0, 3], [1, 9], [2, 6]]))