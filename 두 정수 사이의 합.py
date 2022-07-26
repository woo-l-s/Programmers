import random
import re



def solution(a ,b):
    ans = 0
    if a > b:
        for i in range(b, a+1):
            ans+=i
    elif b > a:
        for i in range(a, b+1):
            ans+=i
    else:
        return a
    return ans



a = 3
b = 5

r = solution(a,b)
print(r)

