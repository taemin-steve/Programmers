def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for _ in range(len(citations)):
        if citations[h] >= h + 1:
            h += 1
        else:
            break

    return h
