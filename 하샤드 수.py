# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long


def solution(arr):
    list = []
    arr=str(arr)
    for i in arr:
        list.append(int(i))
    print(list)
    if int(arr) % sum(list) == 0:
        return True
    else:
        return False



arr = 1023
k = solution(arr)
print(k)

# 65~122