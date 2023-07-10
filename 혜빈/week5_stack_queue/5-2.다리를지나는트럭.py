def solution(bridge_length, weight, truck_weights):
    answer = 0 #경과시간
    bridge = [0] * bridge_length  # 다리를 다리 길이만큼 0으로 채움 
    brgW = 0  # 다리의 현재 무게

    while bridge:
        answer += 1 #while문이 한바퀴 돌 때마다 경과시간 +1
        brgW -= bridge[0] #현재 무게 - 다리에서 내려간 트럭 무게
        bridge.pop(0) #트럭이 순서대로 1개씩 내려감

        if len(truck_weights)!=0: #대기 트럭 리스트가 빌 때까지
            if brgW + truck_weights[0] <= weight:  # 다리 위 + 다음 트럭이 다리 지탱 무게를 안 넘으면
                bridge.append(truck_weights.pop(0)) #다음 트럭도 다리로 보냄
                # brgW += truck_weights[0] #다리위 무게 갱신(index error 발생)
                brgW += bridge[-1] #다리위 무게 갱신
            else:  # 넘으면
                bridge.append(0) #0을 채워 다리의 길이 유지
    print(answer)
    return answer
solution(2,10,[7,4,5,6]) #8
solution(100,100,[10]) #101
solution(100,100,[10,10,10,10,10,10,10,10,10,10]) #110