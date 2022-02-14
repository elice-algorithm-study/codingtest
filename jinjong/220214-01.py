from collections import deque

def solution(answers):
    answer = []
    score = {
        'ans1' : 0,
        'ans2' : 0,
        'ans3' : 0
    }
    
    idx = 1
    for i in range(len(answers)):
        if answers[i] == idx:
            score['ans1'] += 1        
        if idx < 5:
            idx += 1
        else:
            idx = 1
    
    dq = deque([1, 3, 4, 5])
    for i in range(len(answers)):
        if i%2==0 and answers[i] == 2:
            score['ans2'] += 1
        elif i%2!=0:
            if answers[i] == dq[0]:
                score['ans2'] += 1
            dq.rotate(-1)
    
    dq3 = deque([3, 1, 2, 4, 5])
    for i in range(len(answers)):
        if i%2==0 and answers[i] == dq3[0]:
            score['ans3'] += 1
        elif i%2!=0:
            if answers[i] == dq3[0]:
                score['ans3'] +=1
            dq3.rotate(-1)
    
    score = sorted(score.items(), key=(lambda x: x[1]), reverse = True)
    
    for i in range(len(score) - 1):
        if score[i][1] == score[i+1][1]:
            answer.append(i+1)
            answer.append(i+2)
        else:
            answer.append(i+1)
            break
        
    tmp = set(answer)
    answer = list(tmp)
    
    return answer
