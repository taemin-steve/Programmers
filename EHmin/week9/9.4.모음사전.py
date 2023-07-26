import itertools

def solution(word):
    dict = list(itertools.product([ 'A', 'E', 'I', 'O', 'U'], repeat=1)) + list(itertools.product([ 'A', 'E', 'I', 'O', 'U'], repeat=2)) + list(itertools.product([ 'A', 'E', 'I', 'O', 'U'], repeat=3)) + list(itertools.product([ 'A', 'E', 'I', 'O', 'U'], repeat=4)) + list(itertools.product([ 'A', 'E', 'I', 'O', 'U'], repeat=5))
    dict = ["".join(i) for i in dict]
    dict = sorted(dict)
    return dict.index(word) + 1

word = "AAAAE"

print(solution(word))