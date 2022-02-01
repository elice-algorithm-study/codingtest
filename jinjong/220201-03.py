def quick(data):
    if len(data) < 2:
        return data
    res = []
    low = []
    high = []
    pv = data[0]
    for i in range(1, len(data)):
        if data[i] > pv:
            low.append(data[i])
        else:
            high.append(data[i])
    low = quick(low)
    high = quick(high)
    
    res += low
    res += pv
    res += high
    
    return res
    
    
def solution(n):
    str_n = str(n)
    arr = []
    for num in str_n:
        arr.append(num)
    
    answer = ''.join(quick(arr))
    return int(answer)
