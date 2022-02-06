def solution(dartResult):
    answer = []
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    score = {'S' : 1, 'D' : 2, 'T' : 3}
    tmp = ''
    for i in range(len(dartResult)):
        if dartResult[i] in num_list:
            tmp += dartResult[i]
            
        elif dartResult[i] == '*':
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[0] *= 2
                
        elif dartResult[i] == '#':
            answer[-1] *= -1
            
        else:
            answer.append(int(tmp) ** score[dartResult[i]])
            tmp = ''
    
    return sum(answer)
