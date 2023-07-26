from itertools import product 

def solution(word):    
    word_dic = set() # 중복제거를 위해 사용
    for p in product(["","A", "E", "I", "O", "U"], repeat = 5): #         
        word_dic.add("".join(p)) # 
    
    word_dic = sorted(word_dic) # 정렬
    return word_dic.index(word) # index 출력


if __name__ == "__main__":
    word_dic = ['', 'A', 'E','AA', 'AE', 'AI', 'AO', 'AU']
    word_dic= sorted(word_dic)
    print(word_dic)
    