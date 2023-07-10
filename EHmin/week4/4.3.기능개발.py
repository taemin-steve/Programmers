import numpy as np

def solution(progresses, speeds):
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    index = 0
    answer = []
    while(index < len(progresses)):
        progresses = progresses + speeds
        count = 0
        
        while(progresses[index] >= 100):
            index += 1 
            count += 1
            if index == len(progresses):
                break
            
        if count != 0 :
            answer.append(count)
            count = 0
            
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))