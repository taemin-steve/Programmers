from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def solution(arr):
    return sum(arr)/len(arr)

arr = list(map(int,input().strip()))
print(solution(arr))