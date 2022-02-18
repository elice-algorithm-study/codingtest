import sys

n = int(sys.stdin.readline().rstrip())
d = [0] * (n + 1) # 배열 초기화

d[1] = 0 # 1에서 1로 가는 경우는 0가지로 설정

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])