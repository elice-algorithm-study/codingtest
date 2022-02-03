def solution(n, arr1, arr2):
    answer = []
    arr1list = []
    arr2list = []
    
    for i in range(n):
        a = arr1[i]
        num = ""
        if a == 1:
            num += "1"
        while a // 2 >= 1:
            if a // 2 == 1:
                if a % 2 == 0:
                    num += "01"
                    a = a//2
                elif a % 2 == 1:
                    num += "11"
                    a = a//2
                break
            else:
                num += str(a % 2)
                a = a // 2
        if len(num) < n:
            num += "0"* (n-len(num))
        arr1list.append(num[::-1])
    
    # arr1list 	['01001', '10100', '11100', '10010', '01011']
    
    for i in range(n):
        a = arr2[i]
        num = ""
        if a == 1:
            num += "1"
        while a // 2 >= 1:
            if a // 2 == 1:
                if a % 2 == 0:
                    num += "01"
                    a = a//2
                elif a % 2 == 1:
                    num += "11"
                    a = a//2
                break
            else:
                num += str(a % 2)
                a = a // 2
        if len(num) < n:
            num += "0"* (n-len(num))
        arr2list.append(num[::-1])
    
    
    for i in range(n):
        num = ""
        for j in range(n):
            if arr1list[i][j] == "0" and arr2list[i][j] == "0":
                num += " "
            else:
                num += "#"
        answer.append(num)
    
    
    return answer