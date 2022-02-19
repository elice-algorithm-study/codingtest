n = int(input())
arr = []

arr.append(0)
arr.append(1)
arr.append(3)
arr.append(5)

if n < 4:
    print(arr[n])
else:
    for i in range(4, n+1):
        arr.append((arr[i-1] + (arr[i-2]*2))%10007)
    print(arr[n])
