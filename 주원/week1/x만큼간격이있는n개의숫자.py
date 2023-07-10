# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    add_gap = x

    for i in range(0, n):
        answer.append(x)
        x += add_gap

    return answer
