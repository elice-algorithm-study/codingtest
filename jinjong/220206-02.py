def solution(price, money, count):
    i = 1
    while i <= count:
        money -= price*i
        i+=1
    return money * -1 if money < 0 else 0
