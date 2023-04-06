yen = 1000
N = int(input())
rest = yen - N

yen_list = [500,100,50,10,5,1]
result = 0

for _ in yen_list:
    if rest // _ > 0:
        result += rest//_
        rest %= _

print(result)