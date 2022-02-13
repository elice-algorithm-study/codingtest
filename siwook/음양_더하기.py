def solution(absolutes, signs):
    answer = sum(absolutes)
     
    for i in range(len(signs)):
        if signs[i] == False:
            answer -= absolutes[i] * 2

    return answer
  
  
"""
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""
