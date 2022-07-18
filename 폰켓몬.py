import re
from collections import Counter
from itertools import combinations
from itertools import permutations





def solution(nums):
    answer = 0
    length = int(len(nums) / 2)
    nums = set(nums)
    print(nums)
    print(int(length))

    if length > len(nums):
        length = len(nums)

    p = list(combinations(nums, length))
    # print(p)
    answer = len(p[0])
    return answer


def solution(nums):
    canSelect = len(nums) / 2
    data = set()  # 변수를 set 자료형으로 초기화
    for item in nums:
        if len(data) < canSelect and not item in data:
            data.add(item)

    return len(data)


nums = [3,3,3,2,2,2]
# print(solution(nums))
# print(list(combinations(items, 3)))
print(set(nums))
