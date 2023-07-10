def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    return str(int("".join(numbers)))

print(solution([3, 30, 34, 5, 9]))
# 정답
# 3 30 -> 330

# 그냥 sort -> 303
# *2 -> 33 3030 -> 330
# *3 -> 333 303030 -> 330

# 9 991 ->9 991, 9919 / 9가 먼저나와야함
# *2 -> 99 991991 -> 991이 먼저나옴
# *3 -> 999 991991991 -> 9가 먼저나옴 
    