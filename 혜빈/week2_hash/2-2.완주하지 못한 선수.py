def solution(participant, completion):
    answer = ''
    dict={} #hash 함수를 위한 딕셔너리 선언
    hsValue=0 #해시 값을 관리할 변수 선언
    
    for i in participant: #참여자만큼 반복문이 돎
        # print("par: ",hash(i)) 
        dict[hash(i)]=i #참여자의 문자열 hash값을 키로, 문자열을 값으로 딕셔너리에 추가
        hsValue+=hash(i) #변수에 참여자의 해시값을 다 더함
    for j in completion: #완주자만큼 반복문이 돎
        hsValue-=hash(j) #참여자의 해시값을 모두 더한 수 - 완주자의 해시값
    # print(dict)
    # print(hsValue)
    answer=dict.get(hsValue) #참여자 - 완주자 의 값을 value로 하는 key 얻기
    print(answer)
    return answer