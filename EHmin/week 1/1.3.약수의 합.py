from sys import stdin, stdout
input = stdin.readline

def divisor_sum(n):
    sum = 0
    for i in range(n): # 다만 이런식으로 하면 시간 복잡도가 증가한다는 문제.. 대신 중복은 피하기 용이함.
        if n % (i+1) == 0:
            sum += (i +1)
    return sum 

n = int(input())
print(divisor_sum(n))