from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def solution(x,n):
    return list(x*(i+1) for i in range(n))

x, n = map(int, input().split())
print(solution(x,n))