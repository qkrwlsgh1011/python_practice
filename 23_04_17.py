import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = []
def dfs(start):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(start,n+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()

dfs(1)