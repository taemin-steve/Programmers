def solution(arr):
    answer = [] # stack으로 활용 
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        else:
            if answer[-1] == num: # stack에 들어있는 마지막 숫자와 동일한지 확인
                continue #동일한 문자일 경우 무시
            else:
                answer.append(num) # 동일하지 않은 문자일 경우 stack에 추가
    return answer # stack에 출력 

print(solution(	[1,1,3,3,0,1,1] ))

# 빈 배열에 대해 직접 인댁스로 접근하는 경우 에러가 발생하지만, 아래와 같은 접근은 가능하다.
testList = []
print( testList[-1:] == 1) #슬라이싱이 리스트를 제공한다는 점을 활용
# print(testList[-1]) >> 얘는 에러남