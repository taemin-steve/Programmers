import heapq

def solution(operations):
    commandList = []
    for operation in operations:
        if(operation[0] == 'I'):
            #숫자는 정수로 바꿔주고
            commandList.append(int(operation[2:]))
        else:
            #명령어는 string으로
            commandList.append(operation[2:])
    # print(commandList)
    heap = []
    for command in commandList:
        if(command == '1'): #최대값 삭제
            #print(heap)
            if(heap == []):
                # print('최대값 삭제 넘어가')
                pass
            else:
                #최대값 삭제
                # print('최대값 삭제')
                #temp를 만들어서 최대값으로 heap을 만들어줌
                temp = []
                for num in heap:
                    heapq.heappush(temp, -num)
                heapq.heappop(temp)
                temp = list(map(lambda x: -x, temp))
                heap = temp.copy()
        elif(command == '-1'): #최소값 삭제
            #print(heap)
            if(heap == []):
                # print('최소값 삭제 넘어가')
                pass
            else:
                #최소값 삭제
                # print('최소값 삭제')
                heapq.heapify(heap)
                heapq.heappop(heap)
        else: #추가
            # print('추가')
            heap.append(command)
    # print(heap)
    answer = []
    if(heap == []):
        answer = [0,0]
    else:
        answer = [max(heap), min(heap)]
        
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))