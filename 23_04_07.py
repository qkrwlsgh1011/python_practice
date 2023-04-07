# 200이 들어올 때 1~18 + 29
# 1~19까지 더하고 나서 남은 값이 10이기 때문에 18까지만 하고 19+10더하기
S = int(input())
N_sum = 0
temp = 0
while N_sum <= S:
    temp += 1
    N_sum += temp

print(temp - 1)