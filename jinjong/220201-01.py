def solution(arr):
    if len(arr)==1:
        arr[0] = -1
        return arr
    else:
        min = arr[0]
        for num in arr:
            if min > num:
                min = num
        arr.remove(min)
        return arr
