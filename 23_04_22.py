from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    my_doc = [0 for _ in range(len(priorities))] ## 내 문서 위치 알아야해서 만듬
    my_doc[location]=1 # 전체 리스트 중 내문서위치 =1 
    my_doc = deque(my_doc)  
    cnt=0
    while(my_doc): 
        priority = que.popleft() # 문서 pop
        check_my_doc= my_doc.popleft() # 문서 내껀지 유무 pop
        #### 아래 'len(que) >1'은 max함수 사용시 리스트 길이가 2개 이상을 필요로함,이거 없으면 런타임에러뜰수있음. 또, 비교 리스트가 없다는건 마지막에 인쇄했다는 의미.
        if len(que)>1 and  max(que) > priority : # 문서 중요도가 작으면  
            que.append(priority)  # 인쇄 안하고 뒤로 보냄
            my_doc.append(check_my_doc) # 문서 유무도 뒤로 가야징
        else :  ##중요도 베스트여서 인쇄함 
            cnt+=1 # 인쇄 한번 할 때 마다 한개씩 증가
            if check_my_doc == 1 : # 내문서인지 체크 1이면 내꺼임
                answer = cnt # 내문서 뽑은 순서 정답 보내버리고 break
                break
    return answer

print(solution(	[1, 1, 9, 1, 1, 1], 0))