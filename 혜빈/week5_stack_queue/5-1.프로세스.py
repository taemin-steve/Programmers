def solution(priorities, location):
    answer = 0
    q=[] #중요도 순서대로 담을 큐
    # loc=priorities[location]
        
    while priorities: # 우선순위 리스트가 빌 때까지
        mx=max(priorities) #최대값 
        if location==0: #1. location이 0일 때
            if mx>priorities[0]: #최대값이 중요도 배열의 첫번째 순서보다 크다면
                priorities.append(priorities.pop(0)) #삭제 후 뒤로 보내서 추가함
                location=len(priorities)-1 #맨 뒤로 보냈으므로 location 재설정
            else: #최대값이 중요도 배열의 첫번째 순서와 같다면
                q.append(priorities.pop(0)) #최대 중요도 삭제 후 추가
                answer+=1 #순서 +1(0부터 시작하므로)
                break #반복문 탈출
        else: #location이 0이 아니라면(순서가 궁금한 요소가 뒤에 있다면)
            if mx>priorities[0]: #최대값이 첫번째 요소보다 클 때
                priorities.append(priorities.pop(0)) #첫번째 요소를 뒤로 보냄
                location-=1 #앞으로 하나씩 당겨지기 때문에 -1
            else:  #최대값이 첫번째 요소와 같을 때
                q.append(priorities.pop(0)) #q 배열에 추가하고
                location-=1 #앞에서 한개씩 당겨지므로
                answer+=1 #순서 +1
                 
    # print("q: ",q)
    # print("answer: ",answer)
    return answer

solution([3,1,4,2],2) #1 
solution([3,1,4,2],3) #3 1423 4231 231 312 12 21 1 q:4321 
solution([1,1,9,1,1,1],0) #5