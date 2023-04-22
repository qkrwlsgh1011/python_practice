def solution(participant, completion):
    answer = ''
    part_dict = {name : 0 for name in participant}
    for name in participant:
        part_dict[name] += 1
    for name in completion:
        part_dict[name] -= 1
    answer = part_dict.get(1) 
    return answer

solution(["leo", "kiki", "eden"],["eden", "kiki"])