from sys import stdin, stdout
from collections import Counter
input = stdin.readline

def prefix(phone_book):
    # 문자를 sort 하면 119 ,219, 1191 순이 아닌 119, 1191, 219 순으로 정렬됨!
    # 숫자와 문자열의 정렬의 방향성이 다른것이 point
    phone_book = sorted(phone_book) 
    for i in range(len(phone_book)):
        if i == len(phone_book) - 1:
            break
        prefix = phone_book[i]
        nextWord = phone_book[i+1]
        # prefix로 할당된 문자가 뒷 문자의 가장 앞에 있는지 확인 
        if prefix == nextWord[:len(prefix)]: 
            return False
    return True 

#-------------------------------- Hash 특성(검색이 빠름)이용 -----------------------------------------
def prefix_has(phone_book):
    dict = {}
    for phone_num in phone_book: # prefix 가능 후보군을 전부 dict으로 생성 
        dict[phone_num] = 1
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            if phone_num[:i] in dict: # dict셔너리에의 검색이 list에서의 검색보다 빠름 
                return False
    return True
# 검색기능을 활용하고 싶은경우, dict 구조로 하는 것이 훨씬 효율적일 수 있다. >> 리스트로 하는 경우 통과 하지 못함.
# 무엇을 key로 할것인가 >> unique 한것// 검색하고 싶은것 
#---------------------------------------------------------------------------------

phone_book = ["119", "97674223", "1195524421"]
print(prefix_has(phone_book)) # 
