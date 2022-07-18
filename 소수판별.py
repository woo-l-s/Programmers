import re
from collections import Counter
from itertools import combinations



def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = list(combinations(nums, 3))
    plus = []
    result = 0
    for i in answer:
        plus.append(sum(i))

    for i in plus:
       if is_prime_number(i) == True:
           result += 1
       else:
           pass

    return result


nums = [1,2,7,6,4]
solution(nums)
# print(list(combinations(items, 3)))

