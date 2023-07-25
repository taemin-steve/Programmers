def solution(answers):
    answer = []
    student_answer = [[],[],[]]
    student_answer[0] = [1,2,3,4,5] * 2000
    student_answer[1] = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] * 625
    student_answer[2] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 500
    
    score = [0,0,0]
    
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == student_answer[i][j]:
                score[i] += 1
                
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)

    return answer

answers = [1,3,2,4,2]

print(solution(answers))