def solution(nums):
    answer = 1
    nums.sort()
    for i in range(len(nums) - 1):
        if answer >= len(nums)/2:
            break
        if nums[i] == nums[i+1]:
            continue
        else:
            answer += 1
            print(nums[i], nums[i+1])
    return answer
