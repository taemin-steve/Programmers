def solution(phone_book):
    answer=True
    dict={}
    for nums in phone_book:
        dict[nums]=1  #각 번호를 key로 선언
    
    for nums in phone_book: #전화번호 목록만큼
        pre="" #접두사를 한 자리씩 더할 변수
        for num in nums: #전화번호의 번호 한자리만큼
            pre+=num #번호 한 자씩 더하기
            # print(pre)
            if pre in dict and pre!=nums: #전화번호부에 있지만 자기자신을 제외한 경우에만
                answer=False 
                # print(pre)
    print(answer)
    return answer

solution(["119", "97674223", "1195524421"])