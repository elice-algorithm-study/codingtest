def solution(nums):
    answer = []
    cnt = 0

    for i in range(len(nums)):
        if nums[i] in answer:
            continue
        else:
            answer.append(nums[i])

    if len(answer) > len(nums) // 2:
        answer = answer[:len(nums) // 2]
        for j in answer:
            cnt += answer.count(j)
    else:
        for k in answer:
            cnt += answer.count(k)

    return cnt


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
