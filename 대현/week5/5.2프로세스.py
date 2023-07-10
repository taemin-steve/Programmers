from collections import deque
def solution(priorities, location):
    answer = []
    pri_loc = []
    index = 0
    #우선순위와 그 인덱스를 튜플로 묶음
    for i in priorities:
        pri_loc.append((i, index))
        index = index + 1
    dq = deque(pri_loc)
    while(dq):
        flag = dq.popleft()
        trigger = True
        for i in dq:
            if(i[0]>flag[0]):
                dq.append(flag)
                trigger = False
                break
        #가장 우선 순위가 높으면 정답 리스트에 넣어줌
        if(trigger):
            answer.append(flag)
    # 정렬 완료됐으면 해당 location 찾아서 순서 리턴
    for i in answer:
        if(i[1]==location):
            return answer.index(i)+1
    
