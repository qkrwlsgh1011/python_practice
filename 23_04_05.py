N = int(input())

# 곱하고 더하는 값이 제일 작게 나와야 하기 때문에 
# B가 젤 클 때 A는 젤 작게하고 B가 작을 때 큰 수를 넣는다.
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B 크기 순서대로 index순으로 A를 넣어준다. A -> 오름차순 정렬
A.sort()
sort_B = sorted(B)
max_index = []

for _ in range(N):  # 크기 순 index 출력
    max = sort_B[-(_+1)]
    max_index.append(B.index(max))

result = 0
for _ in range(N):
    idx = max_index[_]
    result += B[idx] * A[_] # B의 최대값 * A의 최솟값

print(result)