from sys import stdin, stdout
from collections import Counter
input = stdin.readline

def clothes_set(clothes):
    # 의상의 카테고리 => key // 해당 카테고리의 의상 수 => value
    my_dict = {}
    result = 1
    for item in clothes:
        if item[1] in my_dict : # 해당 의상의 카테고리가 key에 존재하는 경우 value값 증가 
            my_dict[item[1]] = my_dict.get(item[1]) + 1
        else: # 처음 key를 추가하는 경우 
            my_dict[item[1]] = 1
    for _, value in my_dict.items():
        result *= (value+1) # 안입는 경우도 경우의 수에 포함 하기 위해서 +1
    return result - 1 # 아무것도 입지 않으면 안되기 때문에 -1 해준다

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(clothes_set(clothes))