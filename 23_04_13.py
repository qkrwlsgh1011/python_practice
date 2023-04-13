import sys
input = sys.stdin.readline

V, E = map(int, input().split())

info_lst = [list(map(int, input().split())) for _ in range(E)]
info_lst.sort(key=lambda x : x[2])  # 가중치 오름차순
MST = [] 
parent = [_ for _ in range(V+1)]    # 부모 테이블 0~V

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b] = a
    elif b>a:
        parent[a] = b

for i in range(E):
    if find_parent(parent, info_lst[i][0]) == find_parent(parent, info_lst[i][1]): # 간선 간의 부모가 같으면
        pass
    else:
        MST.append(info_lst[i][2])
        union_parent(parent,info_lst[i][0],info_lst[i][1])

print(sum(MST))