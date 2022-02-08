def solution(sizes):
    tmp = 0
    width = []
    height = []

    for size in sizes:
        if size[0] > size[1]:
            tmp = size[1]
            size[1] = size[0]
            size[0] = tmp
        width.append(size[0])
        height.append(size[1])

    return max(width) * max(height)