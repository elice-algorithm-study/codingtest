def makeWall(num, n):
    arr = []
    while len(arr) < n:
        isWall = num%2
        num = num//2
        if isWall==1:
            arr.append(1)
        else:
            arr.append(0)
    arr.reverse()
    return arr    
    
def solution(n, arr1, arr2):
    answer = []
    Walls = []
    for num in arr1:
        Walls.append(makeWall(num, n))
    for i in range(n):
        arr2_wall = makeWall(arr2[i], n)
        for j in range(n):
            if arr2_wall[j]==1:
                Walls[i][j] = 1
    
    for wall in Walls:
        tmp = ''
        for i in wall:
            if i==1:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    
    return answer
