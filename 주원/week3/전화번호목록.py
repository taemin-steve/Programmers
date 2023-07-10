# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book)

#     for i in range(len(phone_book)-1):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return answer

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
