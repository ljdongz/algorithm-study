import sys

input = sys.stdin.readline

N = int(input()) # 도시 개수

dists = list(map(int, input().split())) # 거리 정보

prices = list(map(int, input().split())) # 주유 가격 정보

cur_price = prices[0] # 현재 가격

cur_dist = dists[0] # 현재 주유 가격으로 계산할 총 거리

total_price = 0 # 누적 금액

cur_loc = 1 # 현재 도시 위치

while cur_loc < N-1:
    # 현재 주유 가격보다 저럼한 도시일 때
    if cur_price > prices[cur_loc]:
        total_price += cur_price * cur_dist
        cur_price = prices[cur_loc]
        cur_dist = dists[cur_loc]
    # 현재 주유 가격이 더 저렴할 때
    else:
        cur_dist += dists[cur_loc]
    
    cur_loc += 1

total_price += cur_price * cur_dist

print(total_price)
    