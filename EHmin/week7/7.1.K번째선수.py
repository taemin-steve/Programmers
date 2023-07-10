def solution(array, commands):
    answer = []
    for command in commands:
        list = array[command[0] - 1 : command[1]]
        list = sorted(list)
        answer.append(list[command[2] - 1]) # 항상 index와 몇번째는 다른점 유의!
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))