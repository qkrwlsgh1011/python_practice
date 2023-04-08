T = int(input())

sec_list = [300,60,10] # 초
cnt_list = []

for _ in sec_list:
    if T // _ >= 1:
        cnt_list.append(T//_)
        T %= _
    else:
        cnt_list.append(0)

if T == 0:
    print(*cnt_list)
else:
    print(-1)