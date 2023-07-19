# 최소직사각형: https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''
모든 명함을 수납할 수 있는 가장 작은 지갑 만들기

풀이 방법
1. size.sort()를 사용하여 각 사각형의 길이를 정렬(각 사이즈마다 가로가 더 작게)
2. max()를 사용하여 큰 값으로 업데이트
'''

def solution(sizes):
    w, h = 0, 0
    for size in sizes:
        size.sort()
        w = max(w, size[0]) 
        h = max(h, size[1])
    return w * h