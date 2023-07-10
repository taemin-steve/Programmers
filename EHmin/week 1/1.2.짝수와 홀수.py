from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def solution(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
def evenOrOdd(num):
    #함수를 완성하세요
    if num%2: # 결과가 0이 아니면 모두 참으로 인식. >> 
        return "Odd"

    return "Even" 
    
num = int(input())
print(solution(num))
