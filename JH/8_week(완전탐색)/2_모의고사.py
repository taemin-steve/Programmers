# 모의고사: https://school.programmers.co.kr/learn/courses/30/lessons/42840

'''
1. 나머지 연산으로 주어진 문제를 채점
2. 가장 많은 점수를 득점한 학생을 뽑은 후 반환
'''

def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5] 
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == student1[i % len(student1)]:
            score[0] += 1
        if answers[i] == student2[i % len(student2)]:
            score[1] += 1
        if answers[i] == student3[i % len(student3)]:
            score[2] += 1
                
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i + 1)

    return answer


if __name__ == '__main__':
    solution([1,2,3,4,5])