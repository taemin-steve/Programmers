# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3

# 소수 찾기
# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numArr = list(numbers)
    permutationSet = set()

    def generatePermutation(arr, visited, string):
        if len(string) > 0:
            permutationSet.add(int(string))

        if len(arr) == len(string):
            return

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                generatePermutation(arr, visited, string + arr[i])
                visited[i] = False

    def isPrime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    generatePermutation(numArr, [False] * len(numArr), '')

    count = 0
    for num in permutationSet:
        if isPrime(num):
            count += 1

    return count
