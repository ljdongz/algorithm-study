def solution(nums: list):
    return min(len(nums)/2, len(set(nums)))