def solution(progresses, speeds):
    answer = []
    queue =[]
    # 각 기능별로 작업이 완료 되는 날짜를 리스트에 생성
    for i in range(len(progresses)):
        if((100-progresses[i]) % speeds[i] == 0):
            queue.append((100-progresses[i]) // speeds[i])
        else:
            queue.append(((100-progresses[i]) // speeds[i])+1)
    n = 0
    flag = queue[0]
    #queue의 수만큼 반복문을 돌면서 조건문 적용
    for _ in range(len(queue)):
        value = queue.pop(0)
        #기준보다 크면 앞에 축적된 원소 개수를 넣어줌
        #새로운 기준 생성, n 초기화
        if(value>flag):
            answer.append(n)
            flag = value
            n = 1
        #작거나 같으면 해당 기능은 같이 끝나는거니깐 축적
        else:
            n = n + 1
        #queue 비었으면 마지막으로 n 넣어주기
        if(len(queue)==0):
            answer.append(n)
            
    return answer
