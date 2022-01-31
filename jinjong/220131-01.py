import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def solution(n, m):
    answer = []
    lnum = max(n, m)
    snum = min(n, m)
    
    if lnum%snum==0:
        answer.append(snum)
        answer.append(lnum)
    else:
        if is_prime(lnum) or is_prime(snum):
            answer.append(1)
            i = 2
            while(True):
                if (lnum*i)%snum==0:
                    answer.append(lnum*i)
                    break
                i+=1
        else:
            i = 2
            while(True):
                if snum%i==0:
                    if lnum%(int(snum/i))==0:
                        answer.append(int(snum/i))
                        break
                i+=1
                
            j = 2
            while(True):
                if (lnum*j)%snum==0:
                    answer.append(lnum*j)
                    break
                j+=1
            
    return answer
