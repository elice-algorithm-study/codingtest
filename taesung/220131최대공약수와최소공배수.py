from math import gcd

def lcm(x, y):
    return x*y // gcd(x,y)

def solution(n, m):
    answer = []
    n_arr = []
    for n_s in range(1, n+1):
        if n % n_s == 0:
            n_arr.append(n_s)

    m_arr = []
    for m_s in range(1, m+1):
        if m % m_s == 0:
            m_arr.append(m_s)

    for i in range(len(n_arr)-1, -1, -1):

        if n_arr[i] in m_arr:
            answer.append(n_arr[i])
            break

    answer.append(lcm(n, m))
    # if n <= m and n in m_arr:
    #     answer.append(m)
    # elif n > m and m in n_arr:
    #     answer.append(n)
    # else:
    #     answer.append(n*m)


    return answer