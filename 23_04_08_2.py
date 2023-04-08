import heapq
import sys

N = int(input())
card_list =[]
for _ in range(N):
    heapq.heappush(card_list, int(sys.stdin.readline()))

# list들의 합이 최소가 되어야 한다.
# a+b = c, c+d = e, e+f = g ----> 그냥 정렬해서 앞에 숫자가 작으면 되는거아닌가?

if len(card_list) == 1:
    print(0)
else:
    answer = 0
    while len(card_list) > 1:
        tmp_1 = heapq.heappop(card_list)
        tmp_2 = heapq.heappop(card_list)
        answer += tmp_1 + tmp_2
        heapq.heappush(card_list, tmp_1+tmp_2)

    print(answer)