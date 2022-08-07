# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long


def solution(n , lost ,reserve):
    l = []
    reserve.sort()
    # 개씨발 reserve2 = reserve 로 했을 경우 reserve에서 요소가 삭제되면 reserve2에서도 같이 삭제됨
    reserve2 = []
    for i in reserve:
        reserve2.append(i)
    for i in reserve2:
        if i in lost:
            print(i)
            lost.remove(i)
            reserve.remove(i)


    for i in range(1, n+1):
        l.append(i)
    k = max(l)
    for i in lost:
        l.remove(i)
    for i in reserve:
        if i-1 in lost:
            l.append(i - 1)
            lost.remove(i-1)
        elif i +1 in lost:
            l.append(i + 1)
            lost.remove(i + 1)
    l = set(l)

    if k+1 in l:
        l.remove(k+1)
    if 0 in l:
        l.remove(0)
    print(l)
    return len(l)




n = 5
lost = [2,4]
reserve = [3,1]
k = solution(n , lost ,reserve)
print(k)
# a, b = map(int, input().strip().split(' '))
# k = a



# 65~122