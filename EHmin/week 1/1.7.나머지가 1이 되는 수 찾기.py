from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def division_1(n):
    x = 0
    while True:
        x += 1
        if (n % x) == 1:
            return x
        
n =  int(input().strip())
print(division_1(n))
        