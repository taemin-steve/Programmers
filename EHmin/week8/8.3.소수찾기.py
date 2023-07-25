import math
import itertools

# 소수 판별 함수
def is_prime_number(a):
    if(a<2):
        return False
    for i in range(2,a):
      if(a%i==0):
        return False
    return True

def solution(numbers):
    candidate = []
    for i in range(len(numbers)):
        nPr = list(itertools.permutations(numbers, i + 1))
        for str in nPr:
            if str[0] == '0':
                if len(str) == 1:
                    continue
                num = int(''.join(str[1:]))
            else:
                num = int(''.join(str))
                
            if is_prime_number(num):
                # print(num)
                candidate.append(num)
    return len(set(candidate))

numbers = "011"
print(solution(numbers))

