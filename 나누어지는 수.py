import random
import re



def solution(arr, divisor):
    sol = []
    for i in arr:
        if (i % divisor) == 0 :
            sol.append(i)
    if len(sol) == 0:
        return -1

    return sorted(sol)



arr = [2, 36, 1, 3]
divisor = 1
r = solution(arr, divisor)
print(r)

