def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    completion.append('tmp')

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
