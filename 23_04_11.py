import sys
input = sys.stdin.readline
n, m = map(int, input().split())

knowList = set(input().split()[1:]) # 진실을 알고 있는 사람의 집합을 knowList
parties = []

for _ in range(m):  # party를 원소로 갖는 배열 parties
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)


cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)
