def getKey(tup):
    return tup[1]

def solution(strings, n):
    answer = []
    arr = []
    strings = sorted(strings)
    for word in strings:
        arr.append((word, ord(word[n])))
        
    arr.sort(key=getKey)
    print(arr)
    for tup in arr:
        answer.append(tup[0])
    
    return answer
