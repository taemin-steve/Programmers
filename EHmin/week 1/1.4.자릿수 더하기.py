from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def add_all_digits(n):
    result = 0 
    while n >= 1:
        result += (n % 10)
        n = n//10 
        print(result)
    return result

# def sum_digit(number):
#     return sum(map(int, str(number)))
# 애초에 이렇게 문자열로 변환해서, 매 문자열마다 int로 변환 가능 
# map()은 iterable 객체를 반환한다. 
    
n = int(input().strip())
print(add_all_digits(n))
print(map(int, str(n)))