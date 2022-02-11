def solution(n, lost, reserve):
    lost_cp = sorted([l for l in lost if l not in reserve])
    reserve_cp = sorted([r for r in reserve if r not in lost])

    for i in reserve_cp:
        for j in lost_cp:
            if j == i - 1:
                lost_cp.remove(j)
            elif j == i + 1:
                lost_cp.remove(j)

    return n - len(lost_cp)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
