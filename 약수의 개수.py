import re
from collections import Counter
from itertools import combinations
from itertools import permutations





def solution(left, right):
    list = []
    answer = 0
    for i in range(left, right+1):
        pandan = 0
        yaksu = []
        for j in range(1, i+1):
            if i % j == 0:
                yaksu.append(j)
                pandan+=1
        # print(yaksu)
        if len(yaksu) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


left = 24
right = 27
r = solution(left, right)
print(r)

