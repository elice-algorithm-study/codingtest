def solution(n):
    answer = 0
    strNum = str(n)
    numlist = []
    
    for i in range(len(strNum)):
        numlist.append(int(strNum[i]))
    answer = sum(numlist)

    return answer