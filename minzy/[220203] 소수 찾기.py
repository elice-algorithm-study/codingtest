# 에라토스테네스의 체: 소수인지 판별하고 싶은 수의 제곱근까지의 배수를 제외시켜주는 방법

def solution(n):
    # 에라토스테네스의 체 초기화: n+1개 요소에 True 설정(소수로 간주)
    answer = [True] * (n + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if answer[i] == True:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i 이후 i의 배수들을 False로 변경
                answer[j] = False

    return len([i for i in range(2, n + 1) if answer[i] == True])  # 0을 제외하기 위해 출력 범위는 2 ~ n+1로 설정

'''
10, 11, 12 실패 / 효율성 테스트 실패
def solution(n):
    answer = []

    for i in range(2, n + 1):  # 2부터 n까지 범위
        cnt = 0  # 각 숫자에 대해 cnt 생성
        for j in range(1, i + 1):  # 다시 1부터 각 숫자까지의 범위 설정
            if i % j == 0:  # 나머지가 0일 때 cnt값 + 1
                cnt += 1
        if cnt <= 2:  # cnt가 2 이하인 값에 대해서만 answer에 append
            answer.append(i)

    return len(answer)
'''