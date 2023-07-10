def solution(phone_book):
    answer = True
    # 주어진 리스트를 사용하여 딕셔너리를 생성
    hashmap = {}
    for phone_number in phone_book:
        hashmap[phone_number] = 1
        
    # 전화번호부의 원소를 하나씩 접근
    for phone_number in phone_book:
        temp = ''
        #전화번호를 한글자씩 접근해서 해쉬함수로 비교
        for number in phone_number:
            temp += number
            #해쉬함수로 접근하는건 O(1)
            if(temp in hashmap and temp != phone_number):
                return False
    return True 
