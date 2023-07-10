def solution(arr):
    answer = []
    
    for i in range(len(arr)): #arr의 길이마다
        if arr[i] not in answer: #arr의 요소가 answer에 없으면
            answer.append(arr[i]) #추가
        elif arr[i]!=arr[i-1]: #arr의 요소와 바로 직전 요소가 같지 않으면(각각 독립적 요소라면)
            answer.append(arr[i]) #answer에 추가
    # print(answer)
    return answer
solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])