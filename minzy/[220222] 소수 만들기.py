def solution(nums):
    answer = []
    cnt = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                res = nums[i] + nums[j] + nums[k]
                answer.append(res)

    for l in answer:
        tmp = 0
        for m in range(1, l + 1):
            if l % m == 0:
                tmp += 1
        if tmp == 2:
            cnt += 1

    return cnt


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
