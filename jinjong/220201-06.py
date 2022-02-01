def func(word):
    for i in range(len(word)):
        if i%2!=0:
            word = word[:i] + word[i].lower() + word[i+1:]
        else:
            word = word[:i] + word[i].upper() + word[i+1:]
    return word

def solution(s):
    answer = ''
    word = ''
    i = 0
    while(i!=len(s)):
        if s[i]==' ':
            if word!='':
                answer += func(word)
                word = ''
            answer += ' '
        else:
            word += s[i]
        if i == len(s)-1:
            if word!='':
                answer += func(word)
            break
        i+=1

    return answer
