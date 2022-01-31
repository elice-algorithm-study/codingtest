def solution(n, m):
    answer = []

    a = max(n, m)
    b = min(n, m)

    while b != 0:
        r = a % b
        a = b
        b = r

    answer = [a, n * m // a]

    return answer

'''
유클리드 호제법
최대공약수: x, y의 최대공약수 = y, r(x%y)의 최대공약수
최소공배수: (x * y) // x, y의 최대공약수
'''