# 문제 전략
# input = N
# 봉지 5,3
# 봉지 최소 수 세기
# case 1 : 5로 한 번에 나뉨
# case 2 : 5로 최대한 나누고 난 나머지 3의 배수
# case 3 : 5로 최대한 - 1 나누고 난 나머지 3의 배수
# case 4 : 안됨.

def divide(total):
    div_max = total//5       # 5로 나눈 몫
    if div_max < 1:         # 5보다 작을 때
        if total % 3 != 0:  # 3으로 안나눠지면 -1 출력
            return -1
        else:
            return total//3  # 3으로 나눠지면 몫 return
    else:                   # 몫이 1 이상
        if total % 5 == 0:  # 5의 배수이면
            return div_max  # 5로 나눈 몫
        else:               # 5로 안나눠짐
            for i in range(div_max,-1,-1):   # 최대한 나누기
                mod = total - 5*i
                if mod%3 == 0:  # 나머지가 3으로 나눠진다면
                    return i + (mod//3)
                else:
                    pass
            return -1       # 5의 배수를 다 돌렸지만 3의 배수가 아님


N = int(input())
print(divide(N))