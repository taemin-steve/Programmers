def solution(sizes):
    W = []
    H = []
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        W.append(sizes[i][0])
        H.append(sizes[i][1])
    return max(W) * max(H)

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes))