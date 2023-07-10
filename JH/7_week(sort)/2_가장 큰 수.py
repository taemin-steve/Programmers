'''
2. 가장 큰 수 : https://school.programmers.co.kr/learn/courses/30/lessons/42746

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.



1. numbers 리스트의 숫자들을 문자열로 변환
2. “000” 을 처리하기 위한 if문
3. sort()를 사용하여 key 조건에 맞게 정렬
   x * 3을 하는 이유
   numbers의 원소는 0 이상 1,000 이하이므로 3자리수로 맞춘 뒤, 비교
4. 정렬된 숫자들을 ''.join(numbers)을 사용하여 하나의 문자열로 연결
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    if set(numbers) == {"0"}:
        return "0"
    numbers.sort(key=lambda x: x * 3, reverse=True)
    largest_num = ''.join(numbers)
    return largest_num