# 양수와,+,-, 괄호를 가지고 식을 만듬
# 괄호를 쳐서 최소 수를 만듬
# - 뒤에는 최대한 크게 + 뒤에는 취대한 작게
input_str = input()
split_sub = input_str.split("-")

answer = 0

# -로 시작하면 -뒤에 나오는 수가 최대여야하기 때문에
split_sum = sum(map(int, (split_sub[0].split('+'))))   

if input_str[0] == '-': # 처음으로 오는 기호가 -일 때
    answer -= split_sum
else:   # -가 나오기 전까지 더하기
    answer += split_sum

for _ in split_sub[1:]: # -가 나오고 나서부터 최대가 되어야함
    _ = sum(map(int, (_.split('+'))))
    answer -= _

print(answer)
