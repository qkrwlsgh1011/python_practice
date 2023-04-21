def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        temp = 0
        if (100 - progresses[i]) % speeds[i] != 0:
            temp = (100 - progresses[i]) // speeds[i] + 1
        else:
            temp = (100 - progresses[i]) // speeds[i]
        answer.append(temp)
    
    tmp_max = answer[0]
    tmp_lst = []
    tmp = 0
    for i in range(len(answer)):
        if answer[i] > tmp_max: # 다음 숫자가 더 크면
            tmp_lst.append(tmp)
            tmp = 1
            tmp_max = answer[i]
        else:       # 다음 숫자가 더 작으면
            tmp += 1
    tmp_lst.append(tmp)
    answer = tmp_lst
    return answer

solution([90, 90, 90, 90], [30, 1, 1, 1])
