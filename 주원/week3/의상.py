def solution(clothes):
    clothList = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in clothList.keys():
            clothList[cloth[1]].append(cloth[0])
        else:
            clothList[cloth[1]] = [cloth[0]]

    for value in clothList.values():
        answer *= len(value) + 1

    return answer-1
