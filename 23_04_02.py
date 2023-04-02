N, K = input().split()
total = int(K)

price_list = []

for i in range(int(N)):
    price = int(input())
    price_list.append(price)

sort_list = reversed(price_list)

count = 0
for price in sort_list:
    if total == 0:
        break
    else:
        if total // price != 0: # 가장 큰 수 나눈 몫이 0이 아니다.
            count = count + (total//price)
            total = total % price
        else:
            pass

print(count)