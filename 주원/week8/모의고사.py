# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1, score2, score3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            score1 += 1
        if answers[i] == s2[i % 8]:
            score2 += 1
        if answers[i] == s3[i % 10]:
            score3 += 1

    max_score = max(score1, score2, score3)
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)

    return answer
