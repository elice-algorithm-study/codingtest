def solution(n):
    num = str(n)
    list = []
    answerlist = []
    answerstr = ""
    answer = 0
    
    for i in range(len(num)):
        list.append(int(num[i]))
    
    for i in range(len(list)):
        big = max(list)
        answerlist.append(str(big))
        list.remove(big)
    
    answer = int(answerstr.join(answerlist))

    return answer