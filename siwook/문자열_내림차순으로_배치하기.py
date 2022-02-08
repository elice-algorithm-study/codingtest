def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse=True)
    s = "".join(s)
    answer += s
    return answer


"""
def solution(s):
    return ''.join(sorted(s, reverse=True))
"""
