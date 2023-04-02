# 사람은 1번부터 N번까지 번호가 매겨져 있으며, 
# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
# 5개의 배열에서 수열의 합이 가장 작은 값 찾기.

def find_min(num_list):
    num_list.sort() # 정렬
    temp_sum = 0
    total_sum = 0
    total_sum_list = []         # 최종 값 list

    for i in range(len(num_list)):
        temp = num_list[i]      # 새롭게 들어오는 숫자
        total_sum_list.append(temp + temp_sum)
        temp_sum = temp + temp_sum    # 다음에 더할 값

    for j in range(len(total_sum_list)):
        total_sum = total_sum_list[j] + total_sum
    return total_sum



N = int(input())
num_list = list(map(int,input().split()))
print(find_min(num_list))