o = "one4seveneight"
t = "23four5six7"
th = "1zerotwozero3"
def solution(s):
    answer = s

    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
    
    for i in arr:
        answer = answer.replace(i, str(arr.index(i)))
            
    return int(answer)

print(solution(t))