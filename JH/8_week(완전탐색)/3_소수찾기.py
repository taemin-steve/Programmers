# 소수 찾기: https://school.programmers.co.kr/learn/courses/30/lessons/42839
'''
풀이 방법
1.  입력 문자열 numbers("013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미)로
    가능한 숫자 생성
2.  각 숫자가 소수 인지 확인하여 개수 반환
'''
    
from itertools import permutations

def perm_num(numbers):
    num_set = set() # 중복 제거를 위한 집합(set)생성
    for i in range(1, len(numbers) + 1): # 서로 다른 길이의 순열을 생성하기 위한 반복문
        for perm in permutations(numbers, i): # 현재 길이의 순열 생성
            number = int(''.join(perm)) # 순열을 문자열로 변환한 뒤 정수로 변환
            num_set.add(number) # 변환된 숫자를 집합에 추가
    print(num_set)
    return num_set

def prime(n):
    if n < 2:
        return False # 2보다 작은 숫자는 소수가 아님
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False # 나누어 떨어지는 숫자가 있으면 소수가 아님 
    return True

def solution(numbers):
    count = 0
    for number in perm_num(numbers): # 순열을 생성하고 각 숫자에 대해 반복
        if prime(number): # 숫자가 소수인지 확인
            count += 1  # 소수인 경우 카운트 증가
    print(count)
    return count

if __name__ == '__main__':
    solution('011')