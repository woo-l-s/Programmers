# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long


def solution(arr):
    idx = 0
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = -1
    arr = [i for i in arr if i not in [-1]]
    print(arr)
    return 0



arr = [4,4,4,3,3]
k = solution(arr)
print(k)
# a, b = map(int, input().strip().split(' '))
# k = a



# 65~122