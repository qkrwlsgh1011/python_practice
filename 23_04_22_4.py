import math

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    total_sqrt = int(math.sqrt(total))
    x = 0
    y = 0
    divide_lst = []
    for i in range(1,total_sqrt+1):
        if total%i == 0:   # 약수이면
            if i == 2 or i == 1: # 노란색이 들어갈 공간이 없음
                pass
            else:
                y = i
                x = total//y
                divide_lst.append((x,y))
    for divide in divide_lst:
        brown_temp = divide[0] * 2 + (divide[1]-2) * 2
        if brown == brown_temp:
            answer = divide
            break
        
    return answer

solution(10,2)