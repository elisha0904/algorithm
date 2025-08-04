def solution(arr):
    if len(arr) <= 1:
        return [-1]
    min_x = min(arr)
    arr.pop(arr.index(min_x))
    return arr