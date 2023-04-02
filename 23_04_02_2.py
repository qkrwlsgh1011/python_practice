# 회의 최대 개수를 출력
# 최대한 아다리가 맞게 회의가 짜여져야 함
# [[a,b],[c,d],[e,f]....]
from collections import namedtuple

N = int(input())

class meeting:
    def __init__(self,start,end):
        self.start = start
        self.end = end

def compare(a,b):       # 클래스 2개 비교
    if a.end == b.end:
        if a.start > b.start:
            return True,b
    elif a.end > b.end:
        return True,b
    else:
        return False,a
    
meeting_list = []
for i in range(N):
    first, fin = input().split()
    a = meeting(int(first),int(fin))
    if i>=1:
        x,y = compare(meeting_list[i-1],a)
        if x == True:
            meeting_list.append(a)
        else:
            pass
    else:
        meeting_list.append(a)
