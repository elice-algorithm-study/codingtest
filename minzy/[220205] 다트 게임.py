def solution(dartResult):
    answer = []
    score = ['S', 'D', 'T']
    option = ['*', '#']

    dartResult = dartResult.replace('10', '@')

    for i in range(len(dartResult)):
        if dartResult[i] in score:
            if dartResult[i] == score[0]:
                if dartResult[i-1] == '@':
                    answer.append(10 ** 1)
                else: answer.append(int(dartResult[i - 1]) ** 1)
            elif dartResult[i] == score[1]:
                if dartResult[i-1] == '@':
                    answer.append(10 ** 2)
                else: answer.append(int(dartResult[i - 1]) ** 2)
            else:
                if dartResult[i-1] == '@':
                    answer.append(10 ** 3)
                else: answer.append(int(dartResult[i - 1]) ** 3)
        elif dartResult[i] in option:
            if dartResult[i] == option[0]:
                if len(answer) >= 2:
                    answer[-1] = answer[-1] * 2
                    answer[-2] = answer[-2] * 2
                else:
                    answer[-1] = answer[-1] * 2
            elif dartResult[i] == option[1]:
                answer[-1] = answer[-1] * (-1)

    return sum(answer)