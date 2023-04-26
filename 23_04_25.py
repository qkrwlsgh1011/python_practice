import sys
import math
import heapq
line_input = sys.stdin.readline
T = int(input())

def heappush(arr, value, index):
    if index == 1:  # 첫번째 인자
        arr.append(value)
    else:
        arr.append(value)
        parent = int(math.log2(index))
        while index != 1 and arr[parent] < arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
            parent = int(math.log2(index))
    

def deleteMax(arr):
    time = 0
    last_idx = len(arr) - 1
    arr[1] = arr[last_idx]
    del arr[last_idx]                           # root를 빼고 마지막 index root에 넣기
    height = int(math.log2(last_idx - 1)) + 1   # 하나 뺐기 때문에 작은 값의 로그값이 높이
    cur = 1
    while cur < 2**(height/2):                  # h/2만큼 부모와 크기비교하지않고 자식끼리 비교
        lchild = cur*2
        rchild = cur*2 + 1
        if arr[lchild] > arr[rchild]:
            arr[cur], arr[lchild] = arr[lchild], arr[cur]
            cur = lchild
        else:
            arr[cur], arr[rchild] = arr[rchild], arr[cur]
            cur = rchild
        time += 1
    
    if arr[cur] > arr[lchild] and arr[cur] > arr[rchild]:
        temp_arr = 
        



for _ in range(T):
    n = int(input())
    candi = [0] + list(map(int, line_input().split()))
    sort_candi = [0]
    for i in range(1,len(candi)):
        heappush(sort_candi,candi[i],i)

    time = 0
    copy_candi = sort_candi
    for i in range(1,len(sort_candi)):
        time += deleteMax(copy_candi) + 1   # 처음 들어갈 때 맨 밑에서 vacant를 올릴 때 무조건 +1 이기 때문에
    del sort_candi[0]
    print(*sort_candi)
    
    
