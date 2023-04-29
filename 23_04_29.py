def solution(answers):
    turn = len(answers)
    first = [1,2,3,4,5]
    first_turn = (turn // len(first) + 1)
    first = first * first_turn
    second = [2,1,2,3,2,4,2,5]
    second_turn = (turn // len(second) + 1)
    second = second * second_turn
    third = [3,3,1,1,2,2,4,4,5,5]
    third_turn = (turn // len(third) + 1)
    third = third * third_turn
    first_result = 0
    second_result = 0
    third_result = 0
    for i in range(len(answers)):
        if first[i] == answers[i]:
            first_result += 1
    for i in range(len(answers)):
        if second[i] == answers[i]:
            second_result += 1
    for i in range(len(answers)):
        if third[i] == answers[i]:
            third_result += 1
    result_lst = []
    result_lst.append(first_result)
    result_lst.append(second_result)
    result_lst.append(third_result)
    answer = []
    for i,v in enumerate(result_lst):
        if v == max(result_lst):
            answer.append(i+1)
    return answer

print(solution([1,3,2,4,2]))