from collections import deque

def solution(bridge_length, weight, truck_weights):
    cur_time = 0
    total_weight = 0

    doing_truck_queue = deque()
    before_truck_queue = deque(truck_weights)

    while doing_truck_queue or before_truck_queue:
        cur_time += 1

        if doing_truck_queue and cur_time - doing_truck_queue[0][0] == bridge_length:
            truck = doing_truck_queue.popleft()
            total_weight -= truck[1]

        if before_truck_queue and total_weight + before_truck_queue[0] <= weight:
            truck = before_truck_queue.popleft()
            total_weight += truck
            doing_truck_queue.append((cur_time, truck))

    return cur_time