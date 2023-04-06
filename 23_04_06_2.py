# 2개의 로프 중량 w면 로프에는 w/2만큼 중량이 걸림
# 한 개의 로프만 골라도됨
# 들어올릴 수 있는 최대 중량
# 만약 로프가 여러개 들어왔는데 중량을 최대 갯수로 나눈게 로프들 중 가장
# 중량을 적게 버티는 로프보다 작아야함
# 하지만 하나가 너무 작게된다면 그걸 안쓰고 하는게 나을수도
N = int(input())

rope_lst = []
for _ in range(N):
    rope_lst.append(int(input()))

rope_lst.sort(reverse=True)
hvy_max = 0
# 로프 1개 쓸 때 (가장 무거운 로프x1)
# 로프 2개 쓸 때 (2번째로 무거운 로프 x 2)
# 로프 3개 쓸 때 (3번째로 무거운 로프 x 3)
for _ in range(1,N+1):  # 쓰는 로프의 개수 적어도 한개 이상은 써야함
    hvy = rope_lst[_ - 1] * _  # 최대 하중
    if hvy > hvy_max:
        hvy_max = hvy

print (hvy_max)