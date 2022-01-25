lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    correct_num = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    
    return [7-max(correct_num + zero, 1), 7-max(correct_num, 1)]