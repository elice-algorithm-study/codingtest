def solution(n):
    answer = 0

    n = map(int, list(str(n)))
    answer = sum(n)
    return answer


"""
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
"""
