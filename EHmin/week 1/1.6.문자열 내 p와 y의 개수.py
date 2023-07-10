from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def check_numberOf_py(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False
    
# def numPY(s):
#     # 함수를 완성하세요
#     return s.lower().count('p') == s.lower().count('y')
# 위에서와 같이 참 거짓을 return 하는 경우 분기문 쓸필요없이 return에서 바로 가능 
      
s = input()
print(check_numberOf_py(s))