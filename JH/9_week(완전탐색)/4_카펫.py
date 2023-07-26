#  https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total = brown + yellow # 전체 넓이
    for h in range(3, int(total ** 0.5) + 1): # 최소 길이 ~ 정사각형        
        if total % h != 0:
            continue 
        w = total // h
        if (h - 2) * (w - 2) == yellow: # 가로와 세로의 길이에서 -2씩 뺀 뒤 곱해 나온 결과가 노란색 영역의 넓이와 같아야함
            return [w,h]
        

