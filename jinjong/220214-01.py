from collections import deque

def solution(answers):
    answer = []
    score = []
    ans1 = ans2 = ans3 = 0
    
    idx = 1
    for i in range(len(answers)):
        if answers[i] == idx:
            ans1 += 1        
        if idx < 5:
            idx += 1
        else:
            idx = 1
    score.append((1, ans1))
    
    dq2 = deque([1, 3, 4, 5])
    for i in range(len(answers)):
        if i%2==0:
            if answers[i] == 2:
                ans2 += 1
            continue

        elif i%2!=0 and answers[i] == dq2[0]:
            ans2 += 1
        dq2.rotate(-1)
    score.append((2, ans2))
    
    dq3 = deque([3, 1, 2, 4, 5])
    for i in range(len(answers)):
        if i%2==0:
            if answers[i] == dq3[0]:
                ans3 += 1
            continue
            
        elif i%2!=0 and answers[i] == dq3[0]:
            ans3 +=1
        dq3.rotate(-1)
    score.append((3, ans3))
    
    maxNum = max(ans1, ans2, ans3)
    for i in range(len(score)):
        if score[i][1] == maxNum:
            answer.append(score[i][0])
        
    return answer
