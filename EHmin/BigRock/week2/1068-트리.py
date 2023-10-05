# 리프노드의 개수를 돌려달라 
# 각노드의 부모가 주어짐 
# 단방향 연결인데, 어 그지 단방향 연결이야 

#DFS인가 ? BFS로 가야하는가? 큐로 집어 넣고 돌리면 되는건가 
# [[1,2],[3,4],[],[],[]]
import sys
sys.setrecursionlimit(50)
    
def DFS(start, tree):
    # print(start)
    global leaf
    if not tree[start]:
        # print("리프노드 " , start)
        leaf += 1
        return 0 
    if tree[start][0] == -1:
        # print("삭제된 노드 ", start)
        return 0
    for node in tree[start]:
        DFS(node, tree)


N = int(input())

tree = [[]for _ in range(N)]

in_list = list(map(int, input().split()))
start = -1 

for i in range(N):
    if in_list[i] == -1:
        start = i
        continue
    tree[in_list[i]].append(i)
    
#노드 삭제, 삭제노드 표기 
d_node = int(input())
for nodes in tree:
    if d_node in nodes:
        nodes.remove(d_node)

tree[d_node].clear()
tree[d_node].append(-1)

# print(tree)
leaf = 0
DFS(start, tree)
print(leaf)
 