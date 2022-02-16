from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque()
    
    for prog in progresses:
        dq.append(prog)
    
    complete = 0
    
    while dq:
        while dq:
            if dq[0] >= 100:
                dq.popleft()
                del speeds[0]
                complete += 1
            else:
                break
                
        if complete >= 1:
            answer.append(complete)
            
        for i in range(len(dq)):
            dq[i] += speeds[i]
        
        complete = 0
        
    return answer
