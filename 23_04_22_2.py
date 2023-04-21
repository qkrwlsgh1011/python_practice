from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    wait_truck = []
    wait_truck = deque(wait_truck)
    while queue:
        temp = queue[0]
        while temp < weight and queue:            # 10보다 작을때까지 대기 가능
            truck = queue.popleft()
            temp += truck
            if temp < weight:
                wait_truck.append(truck)    # 같이 지날 수 있는 트럭 list
            else:
                break
        if len(wait_truck) == 1:
            answer += bridge_length
        else:
            answer += bridge_length + len(wait_truck)
            wait_truck.popleft()
    return answer

print(solution(2,10,[7,4,5,6]))