import sys
from collections import deque
input = sys.stdin.readline


def solve():
    for i in range(int(input())):
        n,k = map(int, input().split())  # N = 건물 개수, K = 규칙 개수
        cost = [0] + list(map(int,input().split())) # 건물 짓는 시간
        link = [[] for _ in range(n+1)] # [시작 정점][끝 정점]
        cntLink = [-1] + [0]*(n)
        for j in range(k):
            a,b = map(int, input().split()) 
            link[a].append(b)           # [시작 정점][끝 정점]
            cntLink[b] += 1             # parent 정점 개수
        victory = int(input())

        dp = [0] * (n+1)
        q = deque()                     # 방문한 정점 queue
        for k in range(1,n+1):
            if cntLink[k] == 0:         # 앞에 연결된 점이 없다면
                q.append(k)             # 오른쪽 끝에 정점 넣기
                dp[k] = cost[k]         # 연결된 점이 없으므로 dp에 cost 넣기
    
        while q:
            curNode = q.popleft()       # 1부터 넣기
            for toNode in link[curNode]:# 1로 시작하는 끝 정점들
                cntLink[toNode] -= 1    # 연산이 끝났으므로 parent 개수 빼주기
                dp[toNode] = max(dp[toNode], dp[curNode]+cost[toNode])
                # 끝 정점의 시간과 시작정점 시간+끝 정점의 시간 중 큰값을 넣기
                if cntLink[toNode] == 0:# parent개수가 끝나면
                    q.append(toNode)    # queue에 끝 정점을 넣어주면서 방문체크
            
            if cntLink[victory] == 0:   # 목표하고자 하는 정점의 parent가 더이상 존재하지 않는다
                print(dp[victory])
                break

solve()