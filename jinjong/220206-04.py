def solution(sizes):
    max_size = 0
    max2_size = 0
    for size in sizes:
        if max(size[0], size[1]) > max_size:
            max_size = max(size[0], size[1])
        if min(size[0], size[1]) > max2_size:
            max2_size = min(size[0], size[1])
            
    return max_size * max2_size
