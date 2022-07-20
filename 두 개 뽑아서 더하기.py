import random
import re
from collections import Counter
from itertools import combinations
from itertools import permutations



def solution():

    l = list(permutations(numbers, 2))
    k = []
    for i in l:
        k.append(sum(i))
    # print(set(k))
    k = list(set(k))
    # 차이가 뭐지 이미 set으로 정리 된 거 아닌가?
    # return k
    return sorted(k)


numbers = [2,1,3,4,1]

r = solution()
print(r)

