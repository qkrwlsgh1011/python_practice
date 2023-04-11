# 보석 갯수 N
# 보석 무게 : M, 보석 가격 V
# 가방 최대 무게 C, 가방 갯수 : K
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
# 보석 가격별무게 힙에 저장
jewl = [list(map(int, input().split())) for _ in range(N)]
bag_lst = [int(input()) for _ in range(K)]

# 정렬
jewl.sort(key = lambda x: x[0])
bag_lst.sort()

# 보석 튜플 순서 = 무게 가치
answer = 0
tmp_jewl = []
for bag in bag_lst:
    while jewl and bag >= jewl[0][0]: # 보석 무게 최소가 가방에 들어가는지, 보석이 남아있는지
        heapq.heappush(tmp_jewl, -jewl[0][1])
        heapq.heappop(jewl)
    if tmp_jewl:
        answer += heapq.heappop(tmp_jewl)
    elif not jewl:
        break

print(-answer)