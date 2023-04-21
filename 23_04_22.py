def solution(priorities, location):
    # 우선순위 별로 
    # 뒤에서부터
    answer = 0
    idx_pri = []
    for i in range(len(priorities)):
        idx_pri.append([priorities[i],i])
    idx_pri.sort(key = lambda x : [-x[0],-x[1]])
    for pri in idx_pri:
        if pri[1] != location:
            answer += 1
        else:
            answer += 1
            break
    return answer

print(solution(	[1, 1, 9, 1, 1, 1], 0))