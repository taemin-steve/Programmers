def solution(progresses, speeds):
    answer = [] #여기에 작업 완료되는 순서대로 각 배열에서 빼서 넣기(pop(0) 사용)

    while progresses: #작업 리스트가 빌 때까지
        cnt=0 #배포 기능 개수    
        for i in range(len(progresses)): #작업 내역 업데이트
            progresses[i]=progresses[i]+speeds[i]
        # print(progresses)
        
        for i in range(len(progresses)): #작업 리스트의 개수만큼 
            if progresses and progresses[0]>=100: #작업 리스트가 남아있고 앞 순서가 작업 완료 되면
                cnt+=1 #배포 기능 개수 더하고
                progresses.pop(0) #각 배열에서 앞부터 뺌
                speeds.pop(0)
            
        if cnt!=0: #같은 날에 완료된 기능이 있다면==배포
            answer.append(cnt)
    
    print("answer: ",answer)
    return answer

solution([93,30,55],[1,30,5]) #7일, 3일, 9일 후 완료, (100-prg)%spd 에서 0이면 완료, !0이면 +1: [2,1]
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])# 5,10,1,1,20,1일 후 완료: [1,3,2]



