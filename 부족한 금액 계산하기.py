import random
import re



def solution(price, money, count):
    answer = 0
    sum = 0
    for i in range (count + 1):
        sum += i
    price = price * sum
    if price > money:
        return price - money
    else:
        return 0



price = 3
money = 20
count = 4
r = solution(price, money, count)
print(r)

