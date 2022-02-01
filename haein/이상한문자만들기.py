def solution(s):
    answer = ''
    
    wordlist = s.split(" ")
    eachlist = [None] * len(wordlist)
    
    for i in range(len(wordlist)):
        word =""
        for j in range(len(wordlist[i])):
            print(wordlist[i][j], j, i)
            if j == 0 or j % 2 == 0:
                word = word + wordlist[i][j].upper()
            else :
                word = word + wordlist[i][j].lower()
            eachlist[i] = word
            
    for i in range(len(wordlist)):
        s=s.replace(wordlist[i],eachlist[i])
    
    answer = s
    

    return answer