N = int(input())
str_list =[]
while N!=0:
    str_list.append(input())
    N -= 1

# 비교
# 1. 자릿수가 큰 거 찾기 2. 자릿수가 큰 숫자 중 맨 앞자리가 젤 커야함
# 3. 두 수가 같은 자리가 되었을 때
alpha_dict = {}
for alpha_str in str_list:  # ACDEB이면 A = 10^4 * 9
    square = len(alpha_str) - 1 # 첫째자리수 10제곱
    for alpha in alpha_str:
        if alpha in alpha_dict: # dictionary에 값이 있다면
            alpha_dict[alpha] += pow(10, square)
        else:
            alpha_dict[alpha] = pow(10, square)
        square -= 1

alpha_dict = sorted(alpha_dict.values(), reverse=True)

result = 0
amount = 9

for value in alpha_dict:
    result += value * amount
    amount -= 1

print(result)