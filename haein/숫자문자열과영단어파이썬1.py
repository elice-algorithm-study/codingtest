# 1차
s = "23four5six7"
nlist = []
for i in range(len(s)):
    nlist.append(s[i]) # ['o', 'n', 'e', '4', 's', 'e', 'v', 'e', 'n', 'e', 'i', 'g', 'h', 't']

num = ["0","1","2","3","4","5","6","7","8","9"]
doc = {}

while True:
    quit = 0
       
    for i in range(len(nlist)):
        for n in num:
            if nlist[i] == n:
                doc[i] = str(n) # 딕셔너리에 찾아야 하는 값을 value로 넣어주고 key값으로는 이미 존재하는 것을 넣어주는 게 편함
                nlist[i] = "-"
    #print(nlist) # ['-', '-', 'f', 'o', 'u', 'r', '-', 's', 'i', 'x', '-']
    
    for n in num :
        if n not in nlist :
            quit = 1
            break
    if quit == 1:
        break 
    
nstr = ""
nstr = nstr.join(nlist)

dic = {"zero": "0", "one":"1","two":"2","three":"3","four":"4","five":"5","six":"6"
       ,"seven":"7","eight":"8","nine":"9"}


for i in range(len(dic)):
    key = list(dic.keys())
    if key[i] in nstr:
        print(key[i], dic[key[i]])
        nstr.replace("four", "6") # replace('old문자열', 'new문자열')
        print(nstr)

# print(nstr) # --four-six-

# for i in range(len(nstr)): # 문자열도 len() 적용 가능
#     if nstr[i] == "-":
#         nstr.replace("-", doc[i])
#         print(nstr)

                
   