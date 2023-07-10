# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True

    pCount = len(s.split("p"))+len(s.split("P"))-2
    yCount = len(s.split("y"))+len(s.split("Y"))-2

    return False if pCount != yCount else True
