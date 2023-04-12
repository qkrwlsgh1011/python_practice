import sys
input = sys.stdin.readline
V = int(input())
Nodes = [[] for _ in range(V+1)]

# 트리 구현
for i in range(V):
    ipt_list = list(map(int, input().split()))
    start_Node = ipt_list[0]
    idx = 1
    while ipt_list[idx] != -1:
        end_node, dist = ipt_list[idx],ipt_list[idx+1]
        Nodes[start_Node].append((end_node,dist))
        idx += 2

distance = [-1] * (V+1)
distance[1] = 0

def dfs(x, dist):
    for i in Nodes[x]:
        a,b = i # a = end지점, b = 거리
        if distance[a] == -1:
            distance[a] = dist + b
            dfs(a, dist+b)

dfs(1,0)
start = distance.index(max(distance))
distance = [-1] * (V+1)
distance[start] = 0
dfs(start,0)
print(max(distance))