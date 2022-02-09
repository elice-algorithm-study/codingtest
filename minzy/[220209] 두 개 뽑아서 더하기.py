def solution(numbers):
    answer = []
    answer_set = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer_set = list(set(answer))

    return sorted(answer_set)